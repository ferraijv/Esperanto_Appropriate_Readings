# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:38:46 2019

@author: Jacob
"""
import wikipedia
import re

def create_search_list(n):
    article_titles_to_iterate = []
    while len(article_titles_to_iterate) < n:
        articles = wikipedia.random(1000)
        for article in articles:
            if article not in article_titles_to_iterate:
                article_titles_to_iterate.append(article)
    return(article_titles_to_iterate)
    
    
def create_corpus(article_titles_to_iterate):
    i = 0
    corpus = []
    for search_term in article_titles_to_iterate:
    
        try:
            text = wikipedia.summary(search_term)
            corpus.append(text.encode("utf-8"))
            print(search_term)
            print(i)
            i = i + 1
        except:
            pass
    return(article_titles_to_iterate)
    
def clean_corpus(corpus):
    corpus_one_text = ' '.join(corpus)
    corpus_one_text = corpus_one_text.lower()
    corpus_one_text = re.sub(r'[^\w\s]','', corpus_one_text)
    corpus_one_text = re.sub(r'[\d]','', corpus_one_text)
    
    return(corpus_one_text)
    
    
def count_words(cleaned_corpus):
    unique_words = set(cleaned_corpus.split())
    word_frequency = {}
    for word in unique_words:
        word = word.lower()
        count = cleaned_corpus.count(word)
        word_frequency[word] = count
    return(word_frequency)
        