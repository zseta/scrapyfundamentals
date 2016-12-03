import scrapy


class SampleItem(scrapy.Item):
    quote = scrapy.Field()
    author = scrapy.Field()

class LoginNeedScraper(scrapy.Spider):
    name = 'login'
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'randomuser', 'password': 'topsecret'},
            callback=self.after_login
        )

    def after_login(self, response):
        if "Error while logging in" in response.body:
            self.logger.error("Login failed!")
        else:
            self.logger.error("Login succeeded!")
            item = SampleItem()
            item["quote"] = response.css(".text").extract()
            item["author"] = response.css(".author").extract()
            return item