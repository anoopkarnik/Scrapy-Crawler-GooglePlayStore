from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from insta.items import InstagramProfileItems
import re
import json

from scrapy import Spider

from insta.utils import get_extracted

class Instagram(Spider):
    name = "instagram"
    start_urls = ["http://instagram.com/nike/"]

    download_delay = 0.5

    def parse(self, response):
        javascript = "".join(response.xpath('//script[contains(text(), "sharedData")]/text()').extract())
        json_data = json.loads("".join(re.findall(r'window._sharedData = (.*);', javascript)))
        items = []
        item = InstagramProfileItems()
        data = get_extracted(json_data["entry_data"]["ProfilePage"])

        item["username"] = data["user"]["username"]
        item["following"] = data["user"]["follows"]["count"]
        item["followers"] = data["user"]["followed_by"]["count"]
        item["profile_picture"] = data["user"]["profile_pic_url"]
        item["full_name"] = data["user"]["full_name"]
        item["id"]  = data["user"]["id"]
        item["biography"] = data["user"]["biography"]
        item["total_posts"] = data["user"]["media"]["count"]
        a = data["user"]["media"]["nodes"]
        i=0
        while i < a.__len__():
            item["Post_id"] = data["user"]["media"]["nodes"][i]["code"]
            item["Caption"] = data["user"]["media"]["nodes"][i]["caption"]
            item["Comments"] = data["user"]["media"]["nodes"][i]["comments"]["count"]
            item["Date"] = data["user"]["media"]["nodes"][i]["date"]
            item["Likes"] = data["user"]["media"]["nodes"][i]["likes"]["count"]
            item["Commenter"] = data["user"]["media"]["nodes"][i]["owner"]["id"]
            item["Picture"] = data["user"]["media"]["nodes"][i]["thumbnail_src"]
            item["Views"] = data["user"]["media"]["nodes"][i]["video_views"]

            items.append(item.copy())
            i += 1
        return items
      

