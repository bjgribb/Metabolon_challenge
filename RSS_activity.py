import datetime
import feedparser

current_time = datetime.datetime.utcnow()

RSS_dict = {
    'BBC': 'http://feeds.bbci.co.uk/news/rss.xml#',
    'ESPN': 'https://www.espn.com/espn/rss/news',
    'CNN': 'http://rss.cnn.com/rss/cnn_topstories.rss',
    'Real Time with Bill Maher': 'http://billmaher.hbo.libsynpro.com/rss',
    'Craigslist': 'https://www.craigslist.org/about/best/all/index.rss',
    'CSS-Tricks': 'http://feeds.feedburner.com/CssTricks',
    'Engadget': 'http://www.engadget.com/rss.xml',
    'Reuters': 'http://feeds.reuters.com/reuters/technologyNews',
    'Mashable': 'http://feeds.mashable.com/Mashable',
}

def getRSStime(rss_url):
    try:
        RSStime = feedparser.parse(rss_url).entries[0].updated_parsed
        return RSStime
    except ValueError:
        RSStime = feedparser.parse(rss_url).entries[0].published.parsed
        return RSStime


print(getRSStime('http://feeds.mashable.com/Mashable'))
print(getRSStime('http://www.engadget.com/rss.xml'))
