# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 19:32:40 2018

@author: ThinkPad
"""
from PIL import Image
import pyscreenshot as ImageGrab
# fullscreen
im=ImageGrab.grab()
im.show()

# part of the screen
im=ImageGrab.grab(bbox=(10,10,500,500))
im.show()

# to file
ImageGrab.grab_to_file('im.png')