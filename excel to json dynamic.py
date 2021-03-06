# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 15:06:15 2019

@author: ThinkPad
"""


import xlrd
from collections import OrderedDict
import simplejson as json
# Open the workbook and select the first worksheet


wb = xlrd.open_workbook('excel-xlrd-sample.xls')
sh = wb.sheet_by_index(0)
# List to hold dictionaries
cars_list = []
# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
    cars = OrderedDict()
    field_names = sh.row_values(0)
    row_values = sh.row_values(rownum)
    for i in range(len(field_names)):
        if row_values[i] != '':
            cars[field_names[i]] = row_values[i]    
    cars_list.append(cars)
# Serialize the list of dicts to JSON
j = json.dumps(cars_list)
# Write to file
with open('data.json', 'w') as f:
    f.write(j)
