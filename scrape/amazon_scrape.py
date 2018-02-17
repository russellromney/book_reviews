#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 10:29:51 2018

@author: rromney
"""


def books_dict_setup(isbns):
    '''build out the beginning of the data dictionary'''
    for isbn in isbns:
        try:
            books_dict[isbn]={
                    "title":'',
                    "book_url":'',
                    "review_urls":[],
                    "reviews": {}
                    }
            # add url
            books_dict[isbn]["book_url"] = "http://www.amazon.com/product-reviews/"+isbn
        except: 
            pass


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


# get ten reviews from one page
def one_page_scrape(isbn):
    '''gets ten reviews' text,url,date,rating (string) from an Amazon review page loaded in the the webdriver'''
    # get the larger review div and the ten individual review divs
    reviews = driver.find_element_by_id('cm_cr-review_list').find_elements_by_class_name('review')
    for i in range(10):
        try:
            #find the review id
            review_number = reviews[i].get_attribute('id')
            # initialize review dictionary
            books_dict[isbn]["reviews"][review_number] = {"review_url":'',"rating":0,"date":'',"text":''}
            # get url, text, date, rating
            books_dict[isbn]["reviews"][review_number]["rating"] = reviews[i].find_element_by_class_name("a-link-normal").get_attribute('title')
            books_dict[isbn]["reviews"][review_number]["text"] = reviews[i].find_element_by_class_name("review-text").text
            books_dict[isbn]["reviews"][review_number]["date"] = reviews[i].find_element_by_class_name("review-date").text
            books_dict[isbn]["reviews"][review_number]["review_url"] = reviews[i].find_element_by_class_name("review-title").get_attribute('href')
        except: 
            pass



def one_book_reviews(isbn):
    '''gets the first 300 Amazon reviews for a book'''
    try:
        # go to the initial review page
        driver.get(books_dict[isbn]["book_url"])
        # get book title
        books_dict[isbn]["title"] = driver.find_element_by_id('cm_cr-brdcmb').find_element_by_class_name('a-link-normal').text
        # scrape ten reviws for 30 pages
        for n in range(30):
            # wait for AJAX
            time.sleep(1)
            # scrape reviews page
            one_page_scrape(isbn)
            # go to the next review page
            driver.find_element_by_class_name('a-last').click()
    except:
        pass
        



def get_amazon_reviews(isbns):
    '''gets 300 Amazon book reviews each books in a list of isbns'''
    # set up dictionary
    books_dict_setup(isbns)
    # scrape reviews for each book
    for isbn in isbns:
        one_book_reviews(isbn)



# get the reviews
import pandas as pd
from selenium import webdriver
import time
import pickle
import json

books_dict = {}
goodreads = pd.read_csv('goodreads_library_export.csv')
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
get_amazon_reviews(isbns)
driver.quit()
# save the data as a pickle file and as a json object
with open("amazon_reviews.p",'wb') as file:
    pickle.dump(books_dict,file)
with open("amazon_reviews.json",'w') as file:
    file.write(json.dumps(books_dict))
    

# to open:
## pickle: assign a new dict object with: this_file = pickle.load(open('amazon_reviews.p','rb'))
## json: assign new object with: this_file = json.load(open('amazon_reviews.json'))