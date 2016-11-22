from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from googleplay.items import GplaycrawlerItem
import urlparse
import copy
class MySpider(CrawlSpider):
  name = "gplay-review"
  allowed_domains = ["play.google.com"]
  start_urls = ["https://play.google.com/store/apps/"]
  rules = [Rule(LinkExtractor(allow=(r'apps',)),follow=True,callback='parse_link')]
    	# r'page/\d+' : regular expression for http://isbullsh.it/page/X URLs
    	#Rule(LinkExtractor(allow=(r'apps')),follow=True,callback='parse_link')]
    	# r'\d{4}/\d{2}/\w+' : regular expression for http://isbullsh.it/YYYY/MM/title URLs
  def abs_url(url, response):
      """Return absolute link"""
      base = response.xpath('//head/base/@href').extract()
      if base:
        base = base[0]
      else:
        base = response.url
      return urlparse.urljoin(base, url)
    
  def parse_link(self,response):
      hxs = HtmlXPathSelector(response)
      titles = hxs.select('/html')
      reviews = []
      for titles in titles:
          review = GplaycrawlerItem()
          review["Item_name"] = ''.join(titles.select('//*[@class="document-title"]/div/text()').extract())
          review["Link"] = ''.join(titles.select('head/link[5]/@href').extract())
          review_text = titles.select('//*[@class="review-text"]//text()').extract()
          review_rating = titles.select('//@aria-label').extract()
          review_date = titles.select('//*[@class="review-date"]/text()').extract()

          i=0
          while i < review_text.__len__():
              if review_text[i] != ' ':
                  review["Date"] = review_date[i]
                  review["Review"] = review_text[i]
                  review["Rating"] = review_rating[i]
                  reviews.append(review.copy())
              i += 1

      return reviews
      

