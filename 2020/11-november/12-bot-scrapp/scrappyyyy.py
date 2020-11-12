# import scrapy

# from scrapy.spiders import XMLFeedSpider
# #from YahooScrape.items import YahooScrapeItem

# class Spider(XMLFeedSpider):
#     name = "YahooScrape"
#     allowed_domains = ["yahoo.com"]
#     start_urls = ('http://rss.jobsearch.monster.com/rssquery.ashx?q=big_data',)    #Crawl BPMX
#     itertag = 'item'

#     def parse_node(self, response, node):
#         self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))

#         item = {}
#         item['title'] = node.xpath('title/text()',).extract_first()                #define XPath for title
#         item['link'] = node.xpath('link/text()').extract_first()
#         item['pubDate'] = node.xpath('link/pubDate/text()').extract_first()
#         item['description'] = node.xpath('description/text()').extract_first()                #define XPath for description
#         return item


import scrapy

linkeru = "./ascraper.xml"

from scrapy.spiders import XMLFeedSpider
#from YahooScrape.items import YahooScrapeItem

class Spider(XMLFeedSpider):
       name = "YahooScrape"
       allowed_domains = ["yahoo.com"]
       start_urls = (linkeru)    #Crawl BPMX
       itertag = 'item'

       def parse_node(self, response, node):
           self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))

           item = {}
           item['title'] = node.xpath('title/text()',).extract_first()                #define XPath for title
           item['link'] = node.xpath('link/text()').extract_first()
           item['pubDate'] = node.xpath('link/pubDate/text()').extract_first()
           item['description'] = node.xpath('description/text()').extract_first()                #define XPath for description
           return item