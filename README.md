
# Brazilian News Websites Scrapping Tool

Tool made to find and download daily news title on the main brazilian news websites (G1, Uol, etc.). It uses the [newspaper library](https://github.com/codelucas/newspaper) for scrapping the websites and returning the articles titles.

The code is structure is as it follows:

### News Manager

Class responsible for reading the URLs array (Which contains all the URLs from the sites analyzed) and passing each one to the *Website Manager* class, in order to receive the articles titles from each website URL. Finally, it appends all the titles in a single array and prints it.

### Website Manager

Class responsible for receiving a single website URL, build it and iterate through all its articles - passing each article URL to the *News Parser* class, which eventually return the title for each article URL.

### News Parser

This class simply receives an article URL, parse it using the newspaper lib referenced above and returns its title.