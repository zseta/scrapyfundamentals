
import scrapy


class BookItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    stock = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()
    tax = scrapy.Field()
    reviews = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()