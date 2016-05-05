# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from store import doubanDB


class BookPipeline(object):
    def process_item(self, item, spider):
        if spider.name != "book":  return item
        if item.get("subject_id", None) is None: return item

        spec = { "subject_id": item["subject_id"] }
        doubanDB.book.update(spec, {'$set': dict(item)}, upsert=True)

        return None
