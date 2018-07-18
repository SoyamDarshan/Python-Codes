# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 23:57:25 2018

@author: soyam
"""

import os
import re
os.chdir('F:\Torrents\One Piece')
a=os.listdir()
print (os.listdir())

for i in a:
    b=re.findall('\d{3}',i)
    print (b[0])
    c=i[i.index('.'):]
    print (c)
    os.rename(i,''.join(["One Piece ",b[0],c]))
    
