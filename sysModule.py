# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 02:02:44 2018

@author: soyam
"""

import sys

sys.stderr.write('test\n')
sys.stderr.flush()
sys.stdout.write('stdout')

print(sys.argv)