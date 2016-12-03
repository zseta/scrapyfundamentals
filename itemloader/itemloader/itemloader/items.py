
import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

class QuoteItem(scrapy.Item):
    text = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst()
    )

    by = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst()
    )

    tags = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(', ')
    )