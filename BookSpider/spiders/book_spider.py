# -*- coding: utf-8 -*-
# @Time    : 2018/3/24 14:44
# @Author  : Hulk Wu
# @File    : book_spider.py


from scrapy import Request
from scrapy.spider import Spider
from BookSpider.items import BookspiderItem


class BookSpider(Spider):
    name = 'douban_books'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://book.douban.com/top250'
        yield Request(url=url, headers=self.headers)

    def parse(self, response):
        item = BookspiderItem()
        books = response.xpath('//div[@class="article"]//tr[@class="item"]')
        for book in books:
            item['name'] = book.xpath('.//a/@title').extract()[0]
            book_infos = book.xpath('./td/p[@class="pl"]/text()').extract()[0]
            split_info = book_infos.split('/')
            item['author'] = split_info[0]
            item['price'] = split_info[-1]
            item['published_time'] = split_info[-2]
            item['published_house'] = split_info[-3]
            item['score'] = book.xpath('.//span[@class="rating_nums"]/text()').extract()[0]
            quote = book.xpath('.//p[@class="quote"]/span[@class="inq"]/text()').extract()
            if quote:
                item['quote'] = quote[0]
            else:
                item['quote'] = "null"
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()[0]
        if next_url:
            yield Request(url=next_url, headers=self.headers)



