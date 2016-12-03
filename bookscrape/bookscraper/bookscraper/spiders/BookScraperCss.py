
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bookscraper.items import BookItem
from w3lib.html import remove_tags


class BookScraperCss(CrawlSpider):
    name = 'bookscraper'
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_css=".nav-list > li > ul > li > a"), follow=True),
        Rule(LinkExtractor(restrict_css=".product_pod > h3 > a"), callback="parse_book")
    )

    def parse_book(self, response):
        book_loader = ItemLoader(item=BookItem(), response=response)
        book_loader.default_input_processor = MapCompose(remove_tags)

        book_loader.add_value("image_urls", response.urljoin(response.css(".item.active > img::attr(src)").extract_first()))

        book_loader.add_css("title", ".col-sm-6.product_main > h1", TakeFirst())
        book_loader.add_css("price", ".price_color", TakeFirst())
        book_loader.add_css("upc", ".table.table-striped > tr:nth-child(1) > td", TakeFirst())
        book_loader.add_css("product_type", ".table.table-striped > tr:nth-child(2) > td", TakeFirst())
        book_loader.add_css("tax", ".table.table-striped > tr:nth-child(5) > td", TakeFirst())
        book_loader.add_css("stock", ".table.table-striped > tr:nth-child(6) > td", TakeFirst())
        book_loader.add_css("reviews", ".table.table-striped > tr:nth-child(7) > td", TakeFirst())
        book_loader.add_css("rating", ".star-rating::attr(class)", TakeFirst())
        return book_loader.load_item()