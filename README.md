# book_reviews
Class and data of goodreads and amazon book reviews

This repo has functions and data that allows you to scrape reviews from Amazon and Goodreads given a goodreads library export; it can be worked with very easily to do a lot for whatever you need. I did this originally for CS 479 at the University of Idaho.

Everything is contained within the class book_reviews including data and metadata. Download/clone the whole repo to use the class easily. 

## if you want to scrape amazon reviews or scrape goodreads reviews, use the /scrape folder

The /scrape folder contains the code - 100% from me bytheway, toot my own horn??!! - that did the scraping. As of right now it's been working overtime without number limits on a little-used to see how many reviews it can scrape. We're at over 600,000 right now and working memory is not happy.

`goodreads_scrape.py: `

> has functions culminating in `get_goodreads_reviews` that takes a list of Goodreads book IDs and -- if you work it around a little bit with a Selenium webdriver (chrome, firefox, etc. all valid) -- returns a python dictionary that contains the book, book url, title, and url/text/date/rating for each review.

`amazon_scrape.py: `

> does the same thing 

The dictionary structures are contained as .p pickle files and the JSON are in .json.

Feel free to do some copy/pasta.
