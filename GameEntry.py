# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:58:55 2018

@author: ThinkPad
"""


class GameEntry:

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_score(self):
        return self._score

    def get_name(self):
        return self._name

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)
