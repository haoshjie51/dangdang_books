# README

## 请不要长时间爬取，以免对网站造成损失

说明：

- 本代码为爬取当当网站商品分类里的图书分类（<http://category.dangdang.com/?ref=www-0-C>）

- 在每个分类里面，爬取每本图书的基本信息，包括书名、封面URL、作者、出版时间、出版社等等

  > 注：有些信息是没有的，所以爬到的数据显示为None或null

  

## requirements.txt

```bash
pip install -r requirements.txt
```

## 在bookschina/pipelines 中的MongoDB需改为自己的IP连接

```python
# 默认不写为当前主机的MongoDB
con = MongoClient()
# 示例
con = MongoClient(192.168.211.167)
```

## 启动

```bash
# 在bookschina目录下
scrapy crawl dangdang
```





