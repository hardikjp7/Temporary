#!/bin/python3
 
import math
import os
import random
import re
import sys
import zipfile
os.environ['NLTK_DATA'] = os.getcwd() + "/nltk_data"
import nltk
 
#
# Complete the 'processRawText' function below.
#
# The function accepts STRING textURL as parameter.
#
 
def processRawText(textURL):
    import requests
    response = requests.get(textURL)
   
    words  = nltk.tokenize.word_tokenize(response.text) # Tokenize into words
    lower_words = list(map( str.lower, words))
    noofwords = len(lower_words)
   
    unique_words = set(lower_words)
    noofunqwords = len(unique_words)
   
    wordcov = math.floor(noofwords/noofunqwords)
   
    from collections import Counter
    mostCommon = Counter(lower_words)
    maxfreq= mostCommon.most_common(1)[0][0]
    return noofwords, noofunqwords, wordcov, maxfreq
 
if _name_ == '_main_':
    textURL = input()
 
    if not os.path.exists(os.getcwd() + "/nltk_data"):
        with zipfile.ZipFile("nltk_data.zip", 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())
 
    noofwords, noofunqwords, wordcov, maxfreq = processRawText(textURL)
    print(noofwords)
    print(noofunqwords)
    print(wordcov)
    print(maxfreq)
