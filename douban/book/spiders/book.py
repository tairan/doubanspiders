# -*- coding: utf-8 -*-

import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from items import BookItem


class BookSpider(CrawlSpider):
    name = "book"
    allowed_domains = ["book.douban.com"]
    start_urls = ["http://book.douban.com"]

    rules = (
        Rule(LinkExtractor(allow=r"/subject/\d+/($|\?\w+)"), 
            callback="parse_book", follow=True),
    )

    def parse_book(self, response):
        item = BookItem()
        item["subject_id"] = int(response.url.split("/")[-2])

        return item
