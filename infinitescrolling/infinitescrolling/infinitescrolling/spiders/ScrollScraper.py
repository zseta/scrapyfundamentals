import json
from scrapy import Request, Spider
from infinitescrolling.items import QuoteItem

class ScrollScraper(Spider):
    name = "scrollingscraper"

    quote_url = "http://quotes.toscrape.com/api/quotes?page="
    start_urls = [quote_url + "1"]

    def parse(self, response):
        quote_item = QuoteItem()
        print response.body
        data = json.loads(response.body)
        for item in data.get('quotes', []):
            quote_item["author"] = item.get('author', {}).get('name')
            quote_item['quote'] = item.get('text')
            quote_item['tags'] = item.get('tags')
            yield quote_item

        if data['has_next']:
            next_page = data['page'] + 1
            yield Request(self.quote_url + str(next_page))
