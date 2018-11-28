# book_reviews
Class and data of goodreads and amazon book reviews; Feel free to do some copy/pasta.


This repo has functions and data that allows you to scrape reviews from Amazon and Goodreads given a goodreads library export; it can be worked with very easily to do a lot for whatever you need. I did this originally for CS 479 at the University of Idaho.

Everything is contained within the class book_reviews (in `book_reviews.py`) including data and metadata. Download/clone the whole repo to use the class easily. 

# Objects

### five data files:

`goodreads_library_export.csv` - csv export of my goodreads library as of January 2018

`goodreads_reviews.json` - json file with goodreads reviews for all books in the `goodreads_library_export.csv`

`goodreads_reviews.p` - pickle file of dictionary containing all the goodreads reviews

`amazon_reviews.json` - json file with all amazon reviews of books in goodreads library

`amazon_reviews.p` - pickle file of dictionary containing all the amazon reviews

### two code files
Two files contain the code - 100% from me, no copypasta - that did the scraping:

`goodreads_scrape.py:`
> Combines Selenium with Beautiful Soup; has functions culminating in `get_goodreads_reviews` that takes a list of Goodreads book IDs and -- if you work it around a little bit with a Selenium webdriver (chrome, firefox, etc. all valid) -- returns a python dictionary that contains the book, book url, title, and url/text/date/rating for each review. __TIME USAGE UPDATE: Old version of `goodreads_scrape.py` (before 2/19) time usage in minutes was about n_reviews (.3+1.5)/60, so for my 870 books and 300 reviews each that was _**over 6 days**_; the new version (as of 2/19) combines Selenium with BeautifulSoup/LXML and takes about 25 seconds per book with a decent internet connection, or only **four hours for a performance increase by a factor of 20; a little over 10 reviews per second**__

`amazon_scrape.py: `

> does the same thing; time usage is at about ten reviews per second. Uses only Selenium. Final function is `get_amazon_reviews` that takes list of ISBN-10s. Usage at the bottom of the file.


