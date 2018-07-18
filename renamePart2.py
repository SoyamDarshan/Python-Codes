# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 02:02:09 2018

@author: soyam
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 23:57:25 2018

@author: soyam
"""

import os
import re
os.chdir(r'C:\Users\soyam\Downloads\Video\New Folder')
print(os.getcwd())
a=os.listdir()
#print (os.listdir())
#
#for f in a:
##    b=re.findall('\d{3}',i)
##    print (b[0])
##    c=i[i.index('.'):]
##    print (c)
##    os.rename(i,''.join(["One Piece ",b[0],c]))
##    
#    file_name,file_ext = os.path.splitext(f)
##    print(file_ext,)
#    file_name = file_name.strip()
##    file_name = file_name.replace('_SD[FromAnime]','')
##    file_name = file_name.replace('-S','Season ')
##    file_name = file_name.replace('-',' Episode ')
##    file_name = file_name.replace('English Subbed Kickassanime','')    
#    
#    file_name = file_name.replace('WatchMHA_com_','Boku no Hero Academia Season ')
#    file_name = file_name.replace('_',' Episode ')
#    
#    
#    file_name='{}{}'.format(file_name,file_ext)
#    print(file_name)    
#    
#    
os.rename('New Folder','Boku no Hero Academia Season 3')