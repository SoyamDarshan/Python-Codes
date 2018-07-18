names = ['jeff','gary','jill','smantha']

##for name in names:
##    print('Hello there, ' + name)
##    print (' '.join(['Hello There', name]))
##print (', '.join(names))    

##import os
##location_of_files = 'C:\Users\soyam\OneDrive\Documents\Python Scripts'
##file_name = 'printing.py'
##
##print(location_of_files + '\\' + file_name)
##with open(os.path.join(location_of_files,file_name)) as f:
##        print(f.read())


who = 'Gary'
how_many =12

#Gary bought 12 apples today

#sentence =
#print who, 'bought' ,how_many , 'apples today'
print ('{} bought {} apples today'.format(who,how_many))
