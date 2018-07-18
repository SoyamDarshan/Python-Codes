# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 00:02:11 2018

@author: soyam
"""

import urllib.request
import re

url = 'http://pythonprogramming.net'

values= {'s':'basics',
         'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

#print (respData)


paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))


for eachP in paragraphs:
    print(eachP)