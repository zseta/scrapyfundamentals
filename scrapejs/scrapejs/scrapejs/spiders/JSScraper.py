import scrapy
from scrapy_splash import SplashRequest

from scrapejs.items import QuoteItem

class MySpider(scrapy.Spider):
    name = "jsscraper"

    start_urls = ["http://quotes.toscrape.com/js/"]


    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url,
                                callback=self.parse,
                                endpoint='render.html',
                                args={'wait':0.5})

    def parse(self, response):
        for q in response.css("div.quote"):
            quote = QuoteItem()
            quote["author"] = q.css(".author::text").extract_first()
            quote["quote"] = q.css(".text::text").extract_first()
            quote["tags"] = q.css(".tag::text").extract()
            yield quote