
import scrapy
from scrapy.loader.processors import MapCompose


class BookItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    stock = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()
    tax = scrapy.Field()
    reviews = scrapy.Field()
