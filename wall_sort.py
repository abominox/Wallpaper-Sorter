# Small Python 3 script to sort wallpaper images into folders based on resolution
# Supported filetypes are PNG and JPG.

# DEPENDENCIES
# A Unix shell (bash, zsh, iTerm, etc.)
# Python 3
# python-imaging

from multiprocessing import pool
import os

# import to get image res
from PIL import Image

print ("Python Wallpaper Sorting Script")
print ("")
print ("Sort current directory (0)")
print ("Sort specified directory (1)")
print ("")
print ("Enter a selection (0 or 1): ")

# get current working directory from shell
dir = os.getcwd()




def imageSort():
    for filename in os.getcwd():
        if filename.endswith(".jpg") or filename.endswith(".png"):
            #get resolution of filename image
            if os.path.isdir(put res in here) == False:
                #create folder for res
