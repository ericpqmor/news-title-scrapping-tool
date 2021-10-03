from news_manager import NewsManager
import json

def main():

    # Loads the file containing the array of news websites urls
    urls_file = open('urls.json',)
    urls = json.load(urls_file)["website_urls"]

    # Finds and prints news websites urls
    news_manager = NewsManager()
    news_manager.find_titles(urls)
    news_manager.print_titles()

if __name__ == "__main__":
    main()