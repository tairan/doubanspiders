# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    subject_id = scrapy.Field()
    isbn10 = scrapy.Field()
    isbn13 = scrapy.Field()
    title = scrapy.Field()
    origin_title = scrapy.Field()
    alt_title = scrapy.Field()
    subtitle = scrapy.Field()
    author = scrapy.Field()
    translator = scrapy.Field()
    publisher = scrapy.Field()
    pubdate = scrapy.Field()
    binding = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    pages = scrapy.Field()
    series = scrapy.Field()
    summary = scrapy.Field()
