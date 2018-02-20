#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:53:11 2018

@author: rromney
"""
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



def soup_scrape( ID, soup ):
    '''scrapes all text reviews on one goodreads book landing page'''
    
    for review in soup.find('div',id='bookReviews').find_all('div',class_='review'):
        # make sure it is a text review
        if review.find('span',class_='readable') is not None: 
            # review id
            books_dict[ID]["reviews"][review.get('id')] = {"review_url":'',"rating":0,"date":'',"text":''}
            
            # date
            books_dict[ID]["reviews"][review.get('id')]["date"] = review.find('a',class_='reviewDate').text
            
            # text - makes sure to get the full review
            if review.find('div',class_='readable') is not None:
                books_dict[ID]["reviews"][review.get('id')]["text"] = review.find('span',class_='readable')[1].text
            else: 
                books_dict[ID]["reviews"][review.get('id')]["text"] = review.find('span',class_='readable').text
            
            # url
            books_dict[ID]["reviews"][review.get('id')]["review_url"] = review.find('link').get('href')
            
            # rating
            if review.find('span',class_='staticStars'):
                books_dict[ID]["reviews"][review.get('id')]["rating"] = review.find('span',class_='staticStars').get('title')
            else:
                books_dict[ID]["reviews"][review.get('id')]["review"] = 'none'
        else:
            continue


def get_goodreads_reviews(books):
    '''gets all textual book reviews for a list of books;
    requires a dict object "books_dict" and webdriver "driver" 
    '''
    
    start_time = time.time()
    
    # setup books dict
    books_dict_setup(books)
    
    # scrape reviews
    for ID in books:
        # go to book page
        driver.get(books_dict[ID]["book_url"])
        
        # extract html soup
        soup = BeautifulSoup(driver.page_source,'lxml')
        
        # get title
        books_dict[ID]["title"] = driver.title
        # scrape ten pages of reviews
        for i in range(10): 
            # scrape the page
            soup_scrape(ID, soup)
            
            # make sure it loads, then go to next page
            time.sleep(1.5)
            try:
                driver.find_element_by_class_name('next_page').send_keys(Keys.ENTER)
                time.sleep(.5)
            except:
                pass

    print('time to complete: ',time.time()-start_time)



##### Goodreads #####
            
# import packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas as pd
import pickle
import json

# build the dictionary
books_dict = {}
driver = webdriver.Chrome()
goodreads = pd.read_csv('goodreads_library_export.csv')
books = goodreads['Book Id']
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
##### Goodreads #####
