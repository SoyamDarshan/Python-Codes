# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 23:52:59 2018

@author: soyam
"""

import os

curDir=os.getcwd()

print (curDir)

#os.mkdir('newDir')

import time

time.sleep(2)

os.rename('newDir','newDir2')
time.sleep(2)

os.rmdir('newDir2')