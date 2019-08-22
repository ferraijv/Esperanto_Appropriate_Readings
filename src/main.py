# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:45:43 2019

@author: Jacob
"""
os.chdir('C:/Users/Jacob/esperanto_project/data')

import wikipedia
import pandas as pd
import re
import functions
import os
import csv



wikipedia.set_lang('Eo')

article_titles_to_iterate = create_search_list(10000)

with open('test.csv', mode='w', newline='') as test:
    wr = csv.writer(test, quoting = csv.QUOTE_ALL)
    wr.writerow(article_titles_to_iterate)
    

corpus = create_corpus(article_titles_to_iterate)

cleaned_corpus = clean_corpus(corpus)

word_frequency = count_words(cleaned_corpus)

df = pd.DataFrame.from_dict(word_frequency, orient = 'index', columns = ['count'])

df = df[df.index.str.len() > 1]

df.sort_values(by = ['count'])