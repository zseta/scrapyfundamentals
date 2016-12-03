
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from customnameimage.items import ImageItem


class BookScraperCss(CrawlSpider):

    name = 'imagescraper'

    start_urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html']

    rules = (
        Rule(LinkExtractor(restrict_css=".product_pod > h3 > a"), callback="parse_book"),
    )


    def parse_book(self, response):
        book = ImageItem()
        relative_img_urls = response.css("div.item.active > img::attr(src)").extract()
        book["image_urls"] = self.url_join(relative_img_urls, response)
        book["image_name"] = response.css(".col-sm-6.product_main > h1::text").extract_first()
        return book

    def url_join(self, urls, response):
        joined_urls = []
        for url in urls:
            joined_urls.append(response.urljoin(url))

        return joined_urls