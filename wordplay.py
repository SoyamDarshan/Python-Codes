# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:11:07 2018

@author: ThinkPad
"""

import scrabble

# print all words containing "uu"
#for word in scrabble.wordlist:
#    if "uu" in word:
#        print(word)

print([word for word in scrabble.wordlist if word == word[::-1]])
