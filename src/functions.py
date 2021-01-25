# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:38:46 2019

@author: Jacob
"""
import wikipedia
import re

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
    
    
def create_corpus(article_titles_to_iterate):
    """ Create Corpus
    
    Adds all of the summaries into one giant corpus
    
    """
    i = 0
    corpus = {}
    for search_term in article_titles_to_iterate:
    
        try:
            text = wikipedia.summary(search_term)
            print("Article length: "+ str(len(text)))
            if len(text) > 500: # Only articles with substance
                corpus[search_term] = str(text.strip())
                print("Search tern: " + search_term)
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
  
def create_rankings(texts, df):
    rankings = {}
    for index, row in texts.iterrows():
        ranking = 0
        for x in row['full_text'].split():
            try:
                ranking += 1/df.loc[x]['count']
            except KeyError:
                ranking += 1
            ranking = ranking/len(row['full_text'].split())
        rankings[index] = ranking
        
