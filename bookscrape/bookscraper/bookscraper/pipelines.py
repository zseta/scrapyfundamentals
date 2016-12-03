from scrapy.exceptions import DropItem
from scrapy.exporters import JsonItemExporter, CsvItemExporter


class BookRatingPipeline(object):

    def process_item(self, item, spider):
        rating = str(item["rating"])

        if ("One" in rating):
            item["rating"] = 1

        elif ("Two" in rating):
            item["rating"] = 2

        elif ("Three" in rating):
            item["rating"] = 3

        elif ("Four" in rating):
            item["rating"] = 4

        elif ("Five" in rating):
            item["rating"] = 5

        return item

class StockPipeline(object):

    max_stock = 5

    def process_item(self, item, spider):
        stock = int(filter(str.isdigit, str(item["stock"])))
        if stock > self.max_stock:
            raise DropItem("More than 5 available here:" % item)
        else:
            return item


class JsonPipeline(object):
    def __init__(self):
        self.file = open("books.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class CsvPipeline(object):
    def __init__(self):
        self.file = open("booksdata.csv", 'wb')
        self.exporter = CsvItemExporter(self.file, unicode)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.create_valid_csv(item)
        self.exporter.export_item(item)
        return item

    def create_valid_csv(self, item):
        for key, value in item.items():
            is_string = (isinstance(value, basestring))

            if (is_string and ("," in value.encode('utf-8'))):
                item[key] = "\"" + value + "\""