import json

from pymongo import MongoClient
from itemadapter import ItemAdapter


class DangdangPipeline(object):
    def open_spider(self, spider):
        if spider.name == "dangdang":
            self.f = open('./books.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        if spider.name == "dangdang":
            self.f.write(json.dumps(dict(item), ensure_ascii=False, indent=2) + ',\n')
        return item

    def close_spider(self, spider):
        if spider.name == 'dangdang':
            self.f.close()


class MongoPipeline(object):
    def open_spider(self, spider):
        if spider.name == "dangdang":
            con = MongoClient()
            self.collention = con.dangdang.books

    def process_item(self, item, spider):
        if spider.name == "dangdang":
            self.collention.insert(dict(item))
        return item
