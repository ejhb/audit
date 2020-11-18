import scrapy
from scrapy.spiders import XMLFeedSpider

class Spider(XMLFeedSpider):
       name = "BigDataScrap"
       allowed_domains = ['rss.jobsearch.monster.com']
       start_urls = ['file:///home/joshua/Documents/git-workspace/audit/2020/11-november/12-bot-scrapp/data/feed_audit.xml']   #Crawl BPMX
       itertag = 'item'

       def parse_node(self, response, node):
           self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))

           item = {}
           item['title'] = node.xpath('title/text()',).extract_first()      #define XPath for title
           item['link'] = node.xpath('link/text()').extract_first()
           item['pubDate'] = node.xpath('pubDate/text()').extract_first()
           item['description'] = node.xpath('description/text()').extract_first()       #define XPath for description
           return item