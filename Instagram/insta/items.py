# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

#from scrapy.item import Item, Field
import scrapy


class InstagramProfileItems(scrapy.Item):
    Post_id = scrapy.Field()
    Caption = scrapy.Field()
    id = scrapy.Field()
    username = scrapy.Field()
    biography = scrapy.Field()
    profile_picture = scrapy.Field()
    full_name = scrapy.Field()
    total_posts = scrapy.Field()
    followers = scrapy.Field()
    following = scrapy.Field()
    Comments = scrapy.Field()
    Date = scrapy.Field()
    Likes = scrapy.Field()
    Commenter = scrapy.Field()
    Picture = scrapy.Field()
    Views = scrapy.Field()



