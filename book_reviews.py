#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 13:00:38 2018

@author: rromney
"""

class book_reviews(object):
    
    '''
    Contains data and metadata on the top 300 book reviews from Amazon and Goodreads
    for the 870 books on my (Russell Romney's) Goodreads bookshelves as of 1/30/2017
    '''
    def __init__(self):
        import json
        import pickle
        
        # initialize metadata
        self.metadata = '''
                        title: Goodreads and Amazon book review data
                        subject/keywords: book review data,goodreads, amazon, books, review data, book data, amazon data, goodreads data, scrape reviews, review scraping, scrape goodreads, scrape amazon
                        description: This dataset contains over 400,000 book reviews. The top 300-ish reviews were scraped for 870 books in February 2018. This data can be used for text mining, natural language processing, etc.
                        source: Data scraped from Amazon and Goodreads; the scraping programs built and used for this task can be found at: http://www.github.com/russellromney/books_review_scraping
                        coverage: Sep 2011 - Feb 2018
                        creator: Russell Romney
                        contributor: None yet
                        rights: MIT License
                        data format: JSON
                        official data version: v0.1
                        dataset identifier: DKE83JWLB8
                        
                        
                        '''
        self.title = "Goodreads and Amazon book review data"
        self.subject = "book review data,goodreads, amazon, books, review data, book data, amazon data, goodreads data, scrape reviews, review scraping, scrape goodreads, scrape amazon"
        self.description = "This dataset contains over 400,000 book reviews. The top 300-ish reviews were scraped for 870 books in February 2018. This data can be used for text mining, natural language processing, etc."
        self.source = "Data scraped from Amazon and Goodreads; the scraping programs built and used for this task can be found at: http://www.github.com/russellromney/books_review_scraping"
        self.coverage = 'Sep 2011 - Feb 2018'
        self.creator = "Russell Romney"
        self.contributor = 'None yet'
        self.rights = 'MIT License'
        self.format = 'JSON'
        self.version = 'v0.1'
        self.identifier = 'DKE83JWLB8'
        
    # functions that return data
    def goodreads_data(self):
        with open('goodreads_reviews.json',encoding='utf-8') as data_file:
            return json.loads(data_file.read())
    
    def amazon_data(self):
        with open('amazon_reviews.json',encoding='utf-8') as data_file:
            return json.loads(data_file.read())
            
    def goodreads_dict(self):
        return pickle.load(open('goodreads_reviews.p','rb'))
        
    def amazon_dict(self):
        return pickle.load(open('amazon_reviews.p','rb'))
