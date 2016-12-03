import scrapy
from ajaxscraper.items import QuoteItem

class AjaxScraper(scrapy.Spider):
    name = "ajaxscraper"

    start_urls = ["http://quotes.toscrape.com/search.aspx"]

    def parse(self, response):
        yield scrapy.FormRequest.from_response(response=response,
                                               formdata={'author': 'Steve Martin', 'tag': 'humor'},
                                               callback=self.parse_item)

    def parse_item(self, response):
        quote = QuoteItem()
        quote["author"] = response.css(".author::text").extract_first()
        quote["quote"] = response.css(".content::text").extract_first()
        yield quote