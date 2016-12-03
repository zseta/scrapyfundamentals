import scrapy

from itemloader.items import QuoteItem
from scrapy.loader import ItemLoader


class SampleSpider(scrapy.Spider):
    name = "toscrape"

    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.css(".quote"):
            loader = ItemLoader(item=QuoteItem(), selector=quote)

            loader.add_css("text", ".text")
            loader.add_css("by", ".authoor")
            loader.add_css("tags", ".tag")
            yield loader.load_item()
