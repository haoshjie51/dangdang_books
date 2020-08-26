# Scrapy settings for bookschina project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bookschina'

SPIDER_MODULES = ['bookschina.spiders']
NEWSPIDER_MODULE = 'bookschina.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bookschina (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bookschina.middlewares.BookschinaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'bookschina.middlewares.BookschinaSpiderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'bookschina.pipelines.DangdangPipeline': 300,
   'bookschina.pipelines.MongoPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 图书大分类列表对象
BOOKS_STYLE_LIST = '//div[@class="classify_books"]/div[@class="classify_kind"]'
# 大图书分类名字
BOOKS_BIG_STYLE = './div[@class="classify_kind_name"]/a/text()'
# 小分类列表对象
BOOKS_SMALL_STYLE_LIST = './ul[@class="classify_kind_detail"]'
# 小分类名字
BOOKS_SMALL_STYLE = './li[@name="cat_3"]/a/text()'
# 小分类url地址
BOOKS_SMALL_STYLE_URL = './li[@name="cat_3"]/a/@href'

# 图书信息
BOOKS_LIST = '//ul[@class="bigimg"]/li'

BOOK_TITLE = './p[@class="name"]/a/text()'
BOOK_NOW_PRICE = './p[@class="price"]/span[@class="search_now_price"]/text()'
BOOK_PRE_PRICE = '/p[@class="price"]/span[@class="search_pre_price"]/text()'
BOOK_DISCOUNT = './p[@class="price"]/span[@class="search_discount"]/text()'
BOOK_AUTHOR = './p[@class="search_book_author"]/span/a[@name="itemlist-author"]/text()'
BOOK_PUBLISH_TIME = './p[@class="search_book_author"]/span[2]/text()'
BOOK_PUBLISHING_HOUSE = './p[@class="search_book_author"]/span[3]/a/text()'
BOOK_DETAIL = './p[@class="detail"]/text()'
BOOK_DETAIL_URL = './a/@href'
BOOK_IMG_URL = './a/img/@data-original'

# 下一页
BOOKS_LIST_NEXT_URL = '//li[@class="next"]/a/@href'