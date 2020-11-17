import scrapy


class JobdataSpider(scrapy.Spider):
    name = 'jobdata'
    allowed_domains = ['http://rss.jobsearch.monster.com']
    start_urls = ['http://http://rss.jobsearch.monster.com/']

    def parse(self, response):
        pass
