# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:03:30 2018

@author: ThinkPad
"""

import scrabble
#
#longest = ""
#
#for word in scrabble.wordlist:
#    if list(word) == list(reversed(word)) and len(word) > len(longest):
#        longest = word
#
#print(longest)


longest = ""

for word in scrabble.wordlist:
    if word == word[::-1] and len(word) > len(longest):
        longest = word

print(longest)

