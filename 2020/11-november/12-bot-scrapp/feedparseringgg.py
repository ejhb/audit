import feedparser

rss_url = 'http://rss.jobsearch.monster.com/rssquery.ashx?q=big_data'
parser = feedparser.parse(rss_url)

for entry in parser.entries:
    print('TITRE :  ',entry.title)
    print('LINK :  ',entry.links[0].href)
    print('DESCRIPTION :  ',entry.summary)
    print('-------------------')

