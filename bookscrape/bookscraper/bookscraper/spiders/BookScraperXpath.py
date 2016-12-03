
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bookscraper.items import BookItem
from w3lib.html import remove_tags


class BookScraperXpath(CrawlSpider):
    name = 'bookscraper_xpath'
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_css=".nav-list > li > ul > li > a"), follow=True),
        Rule(LinkExtractor(restrict_css=".product_pod > h3 > a"), callback="parse_book")
    )

    def parse_book(self, response):
        book_loader = ItemLoader(item=BookItem(), response=response)
        book_loader.default_input_processor = MapCompose(remove_tags)
        book_loader.default_output_processor = TakeFirst()

        book_loader.add_xpath("title", "//div[@class='col-sm-6 product_main']/h1")
        book_loader.add_xpath("price", "//p[@class='price_color']")
        book_loader.add_xpath("upc", "//table[@class='table table-striped']/tr[1]/td")
        book_loader.add_xpath("product_type", "//table[@class='table table-striped']/tr[2]/td")
        book_loader.add_xpath("tax", "//table[@class='table table-striped']/tr[5]/td")
        book_loader.add_xpath("stock", "//table[@class='table table-striped']/tr[6]/td")
        book_loader.add_xpath("reviews", "//table[@class='table table-striped']/tr[7]/td")
        book_loader.add_xpath("rating", "//p[@class='instock availability']/following-sibling::p/@class")
        yield book_loader.load_item()