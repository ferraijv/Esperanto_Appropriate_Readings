# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:45:43 2019

@author: Jacob
"""


import wikipedia
import pandas as pd
import re
import sys
sys.path.append("C:/learning/Esperanto_Appropriate_Readings/src")
import functions
import os
import csv

os.chdir('C:/learning/Esperanto_Appropriate_Readings')

wikipedia.set_lang('En')

article_titles_to_iterate = functions.create_search_list(500)

corpus = functions.create_corpus(article_titles_to_iterate)

texts = pd.DataFrame.from_dict(corpus,
                           orient='index',
                           columns=['full_text'])


cleaned_corpus = functions.clean_corpus(texts)

word_frequency = functions.count_words(cleaned_corpus)

df = pd.DataFrame.from_dict(
    word_frequency,
    orient = 'index',
    columns = ['count']
    ).sort_values('count')

# We don't want any words that are wone letter
df = df[df.index.str.len() > 1]





