# -*- coding: utf-8 -*-
"""
Date: Sun Jan 24 20:51:08 2021
"""

import pickle
import wikipedia
import pandas as pd
import re
import numpy as np

def create_search_list(n):
    """ Create Search List
    
    Finds n random terms to search for
    
    """
    
    article_titles_to_iterate = []
    while len(article_titles_to_iterate) < n:
        articles = wikipedia.random(20)
        for article in articles:
            if article not in article_titles_to_iterate:
                article_titles_to_iterate.append(article)
    return(article_titles_to_iterate)
    

def create_corpus(article_titles_to_iterate, corpus={}):
    """ Create Corpus
    
    Adds all of the summaries into one giant corpus
    
    """
    i = 0
    for search_term in article_titles_to_iterate:
    
        try:
            text = wikipedia.summary(search_term)
            print("Article length: "+ str(len(text)))
            if len(text) > 500: # Only articles with substance
                corpus[search_term] = str(text.strip())
                print("Search term: " + search_term)
                print("Number: " + str(i))
            i = i + 1
        except:
            pass
    return(corpus)

def clean_corpus(texts):
    """ Clean Corpus
    
    Clean each of the article summaries and join them together into one
    single corpus
    
    """
    corpus = []
    texts = pd.DataFrame.from_dict(texts,
                           orient='index',
                           columns=['full_text'])
    for key, row in texts.iterrows():
        text = row['full_text']
        corpus.append(text)
    
    corpus_one_text = ' '.join(corpus)
    corpus_one_text = corpus_one_text.lower()
    corpus_one_text = re.sub(r'[^\w\s]','', corpus_one_text)
    corpus_one_text = re.sub(r'[\d]','', corpus_one_text)

    return(corpus_one_text)

def count_words(cleaned_corpus):
    """ Count Words
    
    Get a list of unique words and determine the word frequencies
    
    """
    unique_words = set(cleaned_corpus.split())
    word_frequency = {}
    for word in unique_words:
        word = word.lower()
        count = cleaned_corpus.count(word)
        word_frequency[word] = count
    return(word_frequency)
  
def clean_word_frequency(word_frequency):
    """ Clean Word Frequency
    
    Converts everything into a dataframe
    
    """
    df = pd.DataFrame.from_dict(
        word_frequency,
        orient = 'index',
        columns = ['count']
        ).sort_values('count')
    return(df)

class texts:
    def __init__(self, language):
        self.language = language
        self.articles = {}
        self.word_frequency = pd.DataFrame()
        wikipedia.set_lang(language)
        self.difficulty = {}
    
    def fetch_articles(self, n):
        """ Fetch Articles
        
        Reaches out to wikipedia to try and grab n articles. It will
        only grab articles that are over 500 characters in length
        
        """
        
        article_keywords = create_search_list(n)
        self.articles = create_corpus(article_keywords, self.articles)
        
    def create_word_frequency(self):
        """ Create Word Frequency
        
        Combines all of the text into a single list in order to create
        a word frequency table
        
        """
        
        cleaned_corpus = clean_corpus(self.articles)
        self.word_frequency = count_words(cleaned_corpus)
        self.word_frequency = clean_word_frequency(self.word_frequency)
        self.word_frequency['rank'] = pd.cut(self.word_frequency['count'], bins=10, labels=range(10))
        
    def rank_articles(self):
        """ Rank Articles
        
        Uses the word frequency table to assign a difficulty rank to each
        text
        
        """
        
        self.difficulty = {}
        for k, v in self.articles.items():
            wf_sum = 0.0
            n_words = 0
            for word in v:
                try: 
                    word = word.lower()
                    freq = self.word_frequency[self.word_frequency.index==word]['rank'].values[0]
                    wf_sum += freq
                    n_words += 1
                except IndexError:
                    pass
            self.difficulty[k] = 1/(wf_sum/n_words)
            print("Difficulty Score for "+k+": "+str(1/(wf_sum/n_words)))
        
        
    def saveTexts():
        pickle.save()
        


language = input("What language would you like to learn?")
text = texts(language)
option = 0
while int(option) >= 0:
    option = input(""" 
        Options
        1) Download more articles""")
    if int(option) == 1:
        n = int(input("How many articles: "))
        text.fetch_articles(n)
        text.articles
        text.create_word_frequency()
        text.word_frequency
        text.rank_articles()
                   
