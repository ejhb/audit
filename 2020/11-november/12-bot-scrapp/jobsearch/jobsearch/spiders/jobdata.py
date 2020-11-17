# import scrapy
# import re


# class JobdataSpider(scrapy.Spider):
#         name = 'jobdata'
#         allowed_domains = ['rss.jobsearch.monster.com']
#         start_urls = ['http://rss.jobsearch.monster.com/rssquery.ashx?q=big_data']   #Crawl BPMX
#         itertag = 'item'

#     def parse_node(self, response, node):
#         self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))

#         item = {}
#         item['title'] = node.xpath('title/text()',).extract_first()      #define XPath for title
#         item['link'] = node.xpath('link/text()').extract_first()
#         item['pubDate'] = node.xpath('pubDate/text()').extract_first()
#         item['description'] = node.xpath('description/text()').extract_first()       #define XPath for description
#         item['guid'] = node.xpath('guid/text()').extract_first()  
#         return item

from scrapy import Request
import scrapy
from pprint import pprint
    # start_urls = ['file:///home/joshua/Documents/git-workspace/audit/2020/11-november/12-bot-scrapp/data/dictdata.xml']

class JobdataSpider(scrapy.Spider):
    name = 'jobdata'
    allowed_domains = ['rss.jobsearch.monster.com']

    # Start the crawler at this URLs
    start_urls = ['file:///home/joshua/Documents/git-workspace/audit/2020/11-november/12-bot-scrapp/data/dictdata.xml']
    #start_urls = ['http://rss.jobsearch.monster.com/rssquery.ashx?q={query}']

    thesaurus = ["machine learning", "machine", "learning", "big data", "big", "data"]

    LOG_LEVEL = "INFO"

    def parse(self, response):

        # We stat with this url
        url = self.start_urls[0]

        # Build and send a request for each word of the thesaurus
        for query in self.thesaurus:
            target = url.format(query=query)
            print("fetching the URL: %s" % target)
            if target.startswith("file://"):
                r = Request(target, callback=self.scrapit, dont_filter=True)
            else:
                r = Request(target, callback=self.scrapit)
            r.meta['query'] = query
            yield r

    def scrapit(self, response):
        query = response.meta["query"]

        # Base item with query used to this response
        item = {"query": query}
        print(query, response)

        # Scrap the data
        for doc in response.xpath("//item"):
            item["title"] = doc.xpath("title/text()").extract()
            item["description"] = doc.xpath("description/text()").extract()
            item["link"] = doc.xpath("link/text()").extract()
            item["pubDate"] = doc.xpath("pubDate/text()").extract()
            item["guid"] = doc.xpath("guid/text()").extract()
            #pprint(item, indent=2)
            print("item scraped:", item["title"])
            yield item