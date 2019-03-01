# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:11:07 2018

@author: ThinkPad
"""

import scrabble
import string

# print all words that do not contain double letters
for letter in string.ascii_lowercase:
    exists = False
    for word in scrabble.wordlist:
        if letter * 2 in word:
            exists = True
            break
    if not exists:
        print("There are no English words with a double letter " + letter)
