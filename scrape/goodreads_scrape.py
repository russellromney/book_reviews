#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:57:27 2018

@author: rromney
final version of goodreads scraper
"""



# initialize dictionary keys: book IDs
def books_dict_setup(books):
    for ID in books:
        books_dict[ID]={
                "title":'',
                "book_url":'',
                "review_urls":[],
                "reviews": {}
                }
        # add url
        books_dict[ID]["book_url"] = "http://www.goodreads.com/book/show/"+str(ID)

'''
structure for JSON:
{
 ID:{
    "title":'',
    "book_url":'',
    "review_urls":[],
    "reviews": {
            review_number:{
                    "review_url":review_url,
                    "rating":0,
                    "date":'',
                    "text":''
                    }
        
            
            }
    }
}
'''


def one_page_links(ID):
    # extend list of reviews, or initialize list 
    #driver.get(books_dict[ID]["book_url"])
    time.sleep(1)
    try:
        books_dict[ID]["review_urls"].extend([x.get_attribute("href") for x in driver.find_elements_by_link_text("see review")])
    except:
        books_dict[ID]["review_urls"] = [x.get_attribute("href") for x in driver.find_elements_by_link_text("see review")]
    


def get_review_links(ID):
    for i in range(10):
        time.sleep(1)
        # get links for each page 
        one_page_links(ID)
        # go to next page
        driver.find_element_by_class_name("next_page").click()
        
        
        
def review_scrape(ID):
    review_number = 0
    for review_url in books_dict[ID]["review_urls"]:
        # initialize review dictionary
        books_dict[ID]["reviews"][review_number] = {"review_url":review_url,"rating":0,"date":'',"text":''}
        try:
            # open review page
            driver.get(books_dict[ID]["reviews"][review_number]["review_url"])
            # extract rating, date, and text
            try:
                books_dict[ID]["reviews"][review_number]["rating"] = driver.find_elements_by_class_name("value-title")[1].get_attribute("title")
                books_dict[ID]["reviews"][review_number]["date"] = driver.find_element_by_class_name("dtreviewed").text
                books_dict[ID]["reviews"][review_number]["text"] = driver.find_element_by_class_name("reviewText").text
            except: 
                continue
            review_number += 1
        except:
            continue
        
    

def get_goodreads_reviews(books):
    # setup dictionary
    books_dict_setup(books)
    # build by-book data
    for ID in books_dict.keys():
        # go to book url and scrape title
        driver.get(books_dict[ID]["book_url"])
        books_dict[ID]["title"] = driver.title
        # build list of review urls
        get_review_links(ID)
        # create review ID
        review_scrape(ID)




# scrape the reviews
from selenium import webdriver
import time
import pandas as pd
import pickle
import json

# get the reviews
books_dict = {}
driver = webdriver.Chrome()
books = pd.read_csv('goodreads_library_export.csv')
books = books['Book Id']

## TEMP ##
books = books[:2]
## TEMP## 

get_goodreads_reviews(books)
driver.quit()

# save the data as a pickle file and as a json object
with open("goodreads_reviews.p",'wb') as file:
    pickle.dump(books_dict,file)
with open("goodreads_reviews.json","w") as file:
    file.write(json.dumps(books_dict))

# to open:
## pickle: assign a new dict object with: this_file = pickle.load(open('goodreads_reviews.p','rb'))
## json: assign new object with: this_file = json.load(open('goodreads_reviews.json'))