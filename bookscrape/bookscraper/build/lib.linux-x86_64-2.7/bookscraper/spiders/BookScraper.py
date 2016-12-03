
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bookscraper.items import BookItem
from w3lib.html import remove_tags


class MySpider(CrawlSpider):
    name = 'bookscraper'
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_css=".nav-list > li > ul > li > a"), follow=True),
        Rule(LinkExtractor(restrict_css=".product_pod > h3 > a"), callback="parse_book")
    )

    def parse_book(self, response):
        book_loader = ItemLoader(item=BookItem(), response=response)
        book_loader.default_input_processor = MapCompose(remove_tags)
        book_loader.default_output_processor = TakeFirst()

        book_loader.add_css("title", ".col-sm-6.product_main > h1")
        book_loader.add_css("price", ".price_color")
        book_loader.add_css("upc", ".table.table-striped > tr:nth-child(1) > td")
        book_loader.add_css("product_type", ".table.table-striped > tr:nth-child(2) > td")
        book_loader.add_css("tax", ".table.table-striped > tr:nth-child(5) > td")
        book_loader.add_css("stock", ".table.table-striped > tr:nth-child(6) > td")
        book_loader.add_css("reviews", ".table.table-striped > tr:nth-child(7) > td")
        book_loader.add_css("rating", ".star-rating::attr(class)")
        yield book_loader.load_item()