#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Russell Romney

imports the functions from the individual scrape files and uses them to scrape
the reviews from amazon and goodreads
"""


# import packages
from selenium import webdriver
import time
import pandas as pd
import pickle
import json


# import scraping functions
from amazon_scrape import *
from goodreads_scrape import *






##### Goodreads #####
# build the dictionary
books_dict = {}
driver = webdriver.Chrome()
goodreads = pd.read_csv('goodreads_library_export.csv')
books = goodreads['Book Id']

## TEMP ##
books = books[:2]
## TEMP## 

try:
    get_goodreads_reviews(books)
except:
    driver.quit()
try:
    driver.quit()
except:
    pass

# save the data as a pickle file and as a json object
with open("goodreads_reviews.p",'wb') as file:
    pickle.dump(books_dict,file)
with open("goodreads_reviews.json","w") as file:
    file.write(json.dumps(books_dict))

# to open:
## pickle: assign a new dict object with: this_file = pickle.load(open('goodreads_reviews.p','rb'))
## json: assign new object with: this_file = json.load(open('goodreads_reviews.json'))
##### Goodreads #####









##### Amazon #####
# get the reviews
books_dict = {}
isbns = []
for isbn in goodreads['ISBN']:
    try:
        isbns.append(isbn[2:12])
    except:
        continue

## TEMP ## 
isbns = isbns[:2]
## TEMP ##

driver = webdriver.Chrome()

try:
    get_amazon_reviews(isbns)
except:
    driver.quit()
try:
    driver.quit()
except:
    pass

# save the data as a pickle file and as a json object
with open("amazon_reviews.p",'wb') as file:
    pickle.dump(books_dict,file)
with open("amazon_reviews.json",'w') as file:
    file.write(json.dumps(books_dict))
# to open:
## pickle: assign a new dict object with: this_file = pickle.load(open('amazon_reviews.p','rb'))
## json: assign new object with: this_file = json.load(open('amazon_reviews.json'))
##### Amazon #####
