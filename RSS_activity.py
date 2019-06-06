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

def get_RSS_time(rss_url):
    try:
        RSS_time = feedparser.parse(rss_url).entries[0].updated_parsed
        return RSS_time
    except ValueError:
        RSS_time = feedparser.parse(rss_url).entries[0].published.parsed
        return RSS_time


def get_inactive_RSS_feeds(RSS_dict):
    for k, v in RSS_dict.items():
        latest_RSS_time = get_RSS_time(v)
        print (k, latest_RSS_time)


get_inactive_RSS_feeds(RSS_dict)
