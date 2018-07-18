# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 23:54:08 2018

@author: soyam
"""

    #
#f = open('withHeaders.txt','r')
#f.close()
#print (f.name)          #name of the file

#print (f.mode)           #which mode is it open
    
#print (f.closed)






with open('0rz1fvzww05x.png','rb') as rf:
#    pass                   #this is used to just do nothing pass the statement
    #    f_contents = f.readlines()
#    f_contents = f.read()
#    f_contents = f.readline()    
#    
#    for line in f:
#        print(line)
#
#
#        size_to_read = 15
#        f_contents = f.read(size_to_read)
#        print(f_contents , end='')
#        f.seek(0)
#        f_contents = f.read(size_to_read)
#        print(f_contents)
        
#        while len(f_contents) > 0:
#            print(f_contents , end='$$$')
#            f_contents = f.read(size_to_read)
#     print (f.tell())
#    f.write('exam')
#    f.seek(0)
#    f.write('t')
#    
    
    
    
    with open('0rz1fvzww05x1.png','wb') as wf:
#        for line in rf:
#            wf.write(line)
#   
        chunk_size = 4096
        rf_chunk= rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)