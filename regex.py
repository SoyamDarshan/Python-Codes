# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 23:09:29 2018

@author: soyam
"""

'''
Identifier

\ escape character 
\d = any number
\D = anything but a number
\s = space
\S = anything but a space
\w = any character
\W = anything but a character
. = any character, except a newline
\b = the whitespace around words
\. = a period


Modifiers:
{1,3} we're expecting 1-3 \d
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ Match the end of the string
^ Match the beginning of the string
| either,or example :\d{1-3} |  \w{5-6}
[] range or "variance" example: [A-Za-z],[A-Z],[1-5a-qA-Z]
{x} expecting "x" amount    


White Space Characters:
\n newline
\s space
\t tab
\e escape
\f form feed
\r return

DONT FORGET!;

. + * ? [] $ ^ {} () | \ if you want to use them dont forget to backslash them
    
    
'''



import re

exampleString='''
Jessica is 15 years old, Daniel is 27 years old.
Edward is 7, and his grandfather, Oscar, is 102.
'''


ages = re.findall(r'\d{1,3}',exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)


ageDict={}
x=0
for eachName in names:
    ageDict[eachName]=ages[x]
    x+=1
    
print (ageDict)    
















