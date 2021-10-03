from website_manager import WebsiteManager

class NewsManager:

    def __init__(self):
        self.website_manager = WebsiteManager()
        self.titles = []

    # Find the titles of several news websites
    def find_titles(self, urls):
        titles = []

        for url in urls:
            articles_titles = self.website_manager.get_articles_titles(url)
            titles.extend(articles_titles)

        self.titles = titles

    # Print the local self.titles array members
    def print_titles(self):
        print("The titles found are:")
        print("---------------------")

        for title in self.titles:
            print(title)

        print("----------------------")