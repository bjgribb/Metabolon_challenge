import datetime
import feedparser

current_time = datetime.datetime.utcnow()

RSS_dict = {
    'BBC': ['http://feeds.bbci.co.uk/news/rss.xml#'],
    'ESPN': ['https://www.espn.com/espn/rss/news', 'http://billmaher.hbo.libsynpro.com/rss'],
    'CNN': ['http://rss.cnn.com/rss/cnn_topstories.rss'],
    'Real Time with Bill Maher': ['http://billmaher.hbo.libsynpro.com/rss'],
    'Craigslist': ['https://www.craigslist.org/about/best/all/index.rss'],
    'CSS-Tricks': ['http://feeds.feedburner.com/CssTricks'],
    'Engadget': ['http://www.engadget.com/rss.xml'],
    'Reuters': ['http://feeds.reuters.com/reuters/technologyNews'],
    'Mashable': ['http://feeds.mashable.com/Mashable'],
}

def get_RSS_time(rss_url):
    try:
        RSS_time = feedparser.parse(rss_url).entries[0].updated_parsed
        return RSS_time
    except ValueError:
        RSS_time = feedparser.parse(rss_url).entries[0].published.parsed
        return RSS_time


def get_inactive_RSS_feeds(RSS_dict):
    inactive_RSS_companies = []
    for k in RSS_dict:
        for v in RSS_dict[k]:
            latest_RSS_time = get_RSS_time(v)
            latest_RSS_datetime = datetime.datetime(
                latest_RSS_time.tm_year,
                latest_RSS_time.tm_mon,
                latest_RSS_time.tm_mday,
                latest_RSS_time.tm_hour,
                latest_RSS_time.tm_min,
                latest_RSS_time.tm_sec
            )
            print(k, latest_RSS_datetime)
            time_delta = datetime.timedelta(hours=24)
            if current_time - latest_RSS_datetime > time_delta:
                inactive_RSS_companies.append(k)
    return inactive_RSS_companies


print(get_inactive_RSS_feeds(RSS_dict))
print('current time', current_time)
