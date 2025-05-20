import feedparser
from typing import List

def fetch_news_rss(feed_urls: List[str], max_items: int = 10) -> List[str]:
    """
    Fetches latest news headlines from RSS feeds.
    """
    headlines = []
    for url in feed_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:max_items]:
            headlines.append(entry.title)
    return headlines
