from newspaper import build
from news_parser import NewsParser

class WebsiteManager:

    def __init__(self):
        self.news_parser = NewsParser()

    # Build the news websites objects
    # Then gets its articles
    def get_website_articles(self, website_url):
        news = build(website_url)
        self.articles = news.articles

    # Articles getter
    def get_articles(self):
        return self.articles

    # Articles setter
    def set_articles(self, articles):
        self.articles = articles

    def get_articles_titles(self, website_url):
        self.get_website_articles(website_url)
        titles = []

        # Iterates through all the articles of the url
        for article in self.articles:
            # Gets the article title
            if len(article.title) > 0:
                titles.append(self.news_parser.get_title(article.url))

        return titles