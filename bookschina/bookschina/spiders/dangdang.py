import time

import scrapy
from ..settings import *


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/?ref=www-0-C']
    base_url = 'http://category.dangdang.com'

    def parse(self, response):
        books_style_list = response.xpath(BOOKS_STYLE_LIST)
        for books_style_one in books_style_list[:1]:
            item = {}
            item['b_category'] = books_style_one.xpath(BOOKS_BIG_STYLE).extract_first()
            s_category_list = books_style_one.xpath(BOOKS_SMALL_STYLE_LIST)
            for li in s_category_list:
                # 名字
                item['s_category'] = li.xpath(BOOKS_SMALL_STYLE).extract_first()
                # url
                item['s_category_url'] = li.xpath(BOOKS_SMALL_STYLE_URL).extract_first()
                # 进入url
                books_list = scrapy.Request(
                    url=item['s_category_url'],
                    callback=self.book_parse,
                    meta={'item': item}
                )
                yield books_list

    def book_parse(self, response):
        """图书分类页面数据提取"""
        item = response.meta['item']
        books_list = response.xpath(BOOKS_LIST)
        for li in books_list:
            item['book_name'] =li.xpath(BOOK_TITLE).extract_first()
            item['book_cover'] = li.xpath(BOOK_IMG_URL).extract_first()
            item['book_author'] = li.xpath(BOOK_AUTHOR).extract_first()
            item['book_pubtime'] = li.xpath(BOOK_PUBLISH_TIME).extract_first().split("/")[1] if len(li.xpath(BOOK_PUBLISH_TIME)) > 0 else None
            item['book_price'] = li.xpath(BOOK_NOW_PRICE).extract_first()
            item['book_pre_price'] = li.xpath(BOOK_PRE_PRICE).extract_first()
            item['book_discount'] = li.xpath(BOOK_DISCOUNT).extract_first().split("(")[1][:-2] if len(li.xpath(BOOK_DISCOUNT)) > 0 else None
            item['book_pubhouse'] = li.xpath(BOOK_PUBLISHING_HOUSE).extract_first()
            item['book_detail'] = li.xpath(BOOK_DETAIL).extract_first()
            item['book_url'] = li.xpath(BOOK_DETAIL_URL).extract_first()
            yield item

            next_url = response.xpath(BOOKS_LIST_NEXT_URL).extract_first()
            if next_url is not None:
                time.sleep(3)
                yield response.follow(
                    url=next_url,
                    callback=self.book_parse,
                    meta={'item': item}
                )


