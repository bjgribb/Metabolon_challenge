import datetime
import feedparser

RSS_dict = {
    'BBC': ['http://feeds.bbci.co.uk/news/rss.xml#'],
    'ESPN': ['https://www.espn.com/espn/rss/news', 'http://www.espn.com/espn/rss/nba/news'],
    'CNN': ['http://rss.cnn.com/rss/cnn_topstories.rss'],
    'Real Time with Bill Maher': ['http://billmaher.hbo.libsynpro.com/rss'],
    'Craigslist': ['https://www.craigslist.org/about/best/all/index.rss'],
    'CSS-Tricks': ['http://feeds.feedburner.com/CssTricks'],
    'Engadget': ['http://www.engadget.com/rss.xml'],
    'Mashable': ['http://feeds.mashable.com/Mashable'],
    'NYT': ['http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml', 'http://www.nytimes.com/services/xml/rss/nyt/Business.xml'],
    'Reuters': ['http://feeds.reuters.com/reuters/topNews', 'http://feeds.reuters.com/Reuters/worldNews', 'http://feeds.reuters.com/reuters/technologyNews'],
}

def get_day_delta():
    """Gathers user input for number of days of inactivity and converts to integer"""
    try:
        day_delta = int(input('Please enter the number of days of inactivity you would like to search for (i.e. 1, 2, 3, etc.) '))
        return (day_delta * 24)
    except ValueError:
        print("Uh-oh that wasn't a number please enter a whole number.")
        return get_day_delta()


def get_RSS_time(rss_url):
    """Utilizes feedparser to gather published date of latest entry"""
    try:
        RSS_time = feedparser.parse(rss_url).entries[0].published_parsed
        return RSS_time
    except AttributeError:
        RSS_time = feedparser.parse(rss_url).entries[0].updated_parsed
        return RSS_time


def company_output(inactive_RSS_companies):
    """checks inactive company list and formats print output"""
    if len(inactive_RSS_companies) > 1:
        print('List of inactive company RSS feeds:')
        print('\n'.join(inactive_RSS_companies))
    else:
        print('No inactive company RSS feeds to report.')


def get_inactive_RSS_feeds(RSS_dict):
    """Iterates thru RSS url feeds and compares published time to current time to
    to determine which companies have not been updated in a given number of days"""
    inactive_RSS_companies = []
    current_time = datetime.datetime.utcnow()
    time_delta = datetime.timedelta(hours=get_day_delta())
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
            if current_time - latest_RSS_datetime > time_delta:
                inactive_RSS_companies.append(k)
    return company_output(inactive_RSS_companies)


get_inactive_RSS_feeds(RSS_dict)
