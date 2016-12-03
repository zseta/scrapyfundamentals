from scrapy.spiders import Spider

from ImageScraper.items import BookItem


class BookScraperCss(Spider):
    name = 'imagescraper'
    start_urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html']


    def parse(self, response):
        book = BookItem()
        relative_img_urls = response.css("img.thumbnail::attr(src)").extract()
        book["image_urls"] = self.url_join(relative_img_urls, response)

        return book

    def url_join(self, urls, response):
        joined_urls = []
        for url in urls:
            joined_urls.append(response.urljoin(url))

        return joined_urls