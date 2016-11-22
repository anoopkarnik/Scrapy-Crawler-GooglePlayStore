# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


##class GplaycrawlerPipeline(object):
##    def process_item(self, item, spider):
##        return item

from scrapy import log  
from twisted.enterprise import adbapi  
from scrapy.http import Request  
from scrapy.exceptions import DropItem  
#from scrapy.contrib.pipeline.images import ImagesPipeline  
import time  
import psycopg2 

  
  
class GplayPipeline(object):  
  
    def __init__(self):  
        self.conn = psycopg2.connect("dbname='gplay' user='postgres' host='localhost' password='anoop'")
##        self.links_seen = []

    def process_item(self, item, spider):
        if str(item['Link']).find('details?id') != - 1:
##        if item['Link'] in self.links_seen:
##            raise DropItem("Duplicate item found: %s" % item)
##        else:
##            self.links_seen.append(item['Link'])
          try:
              cur = self.conn.cursor()

              cur.execute("insert into apps_review ( item_name,link, date,  rating,   review) values ( %s, %s,%s,%s, %s)", (item["Item_name"], item["Link"] ,item["Date"], item["rating"],   item["review"]))
              self.conn.commit()
          except:
              self.conn.rollback()
        return item  
