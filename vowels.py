# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:54:17 2018

@author: ThinkPad
"""

import scrabble

vowels = "aeiou"


def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True


for word in scrabble.wordlist:
    if has_all_vowels(word):
        print(word)
