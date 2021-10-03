from newspaper import Article

# This class shall receive a single url and parse its title
class NewsParser:

    # Receives the url and parses the article
    def parse_article(self, url):
        self.article = Article(url)
        self.article.download()
        self.article.parse()

    # Article getter
    def get_article(self):
        return self.article

    # Article setter
    def set_article(self, article):
        self.article = article


    # Returns the article title
    def get_title(self, article_url):
        self.parse_article(article_url)
        return self.article.title
