
from scrapy import signals


class BookschinaSpiderMiddleware:
    def process_request(self, request, spider):

        ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
        request.headers['User-Agent'] = ua

