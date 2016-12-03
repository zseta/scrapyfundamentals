import scrapy
from countryscraper.items import CountryItem
from scrapy.loader import ItemLoader

class SampleSpider(scrapy.Spider):
    name = "country"

    start_urls = ["https://scrapethissite.com/pages/simple/"]

    def parse(self, response):

        for country in response.css(".col-md-4, .country"):
            item = ItemLoader(item=CountryItem(), selector=country)

            item.add_css("country", ".country-name")
            item.add_css("capital", ".country-capital::text")
            item.add_css("population", ".country-population::text")
            item.add_css("area", ".country-area::text")

            yield item.load_item()