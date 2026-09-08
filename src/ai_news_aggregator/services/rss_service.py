import feedparser

from ai_news_aggregator.scrapers.article_scraper import scrape_article_content


RSS_FEEDS = {
    "MIT Technology Review": "https://www.technologyreview.com/feed/",
    "VentureBeat AI": "https://venturebeat.com/category/ai/feed/",
    "TechCrunch AI": "https://techcrunch.com/category/artificial-intelligence/feed/",
}


def fetch_all_news():
    all_articles = []

    for source, url in RSS_FEEDS.items():

        print(f"\nFetching news from: {source}")

        feed = feedparser.parse(url)

        for entry in feed.entries[:10]:

            article_url = entry.get("link", "")

            print(f"Scraping: {entry.get('title', '')}")

            content = scrape_article_content(article_url)

            article = {
                "title": entry.get("title", ""),
                "url": article_url,
                "source": source,
                "content": content or "",
            }

            all_articles.append(article)

    return all_articles