# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import MapCompose
from w3lib.html import remove_tags
from string import strip

class CountryItem(scrapy.Item):
    country = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip),
        output_processor=TakeFirst()
    )
    capital = scrapy.Field(output_processor=TakeFirst())
    population = scrapy.Field(output_processor=TakeFirst())
    area = scrapy.Field(output_processor=TakeFirst())
