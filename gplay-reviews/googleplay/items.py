# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

#from scrapy.item import Item, Field
import scrapy


class GplaycrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = Field()
    Date = scrapy.Field()
    Link = scrapy.Field()
    Item_name = scrapy.Field()
    Rating = scrapy.Field()
    Review = scrapy.Field()





