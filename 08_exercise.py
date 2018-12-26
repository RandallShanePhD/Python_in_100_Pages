# Python in 100 Pages - v2
# Libraries Exercise

import os

# List files of a certain type in a directory
dir = '/Users/randallshane/Pictures/'
file_list = os.listdir(dir)

for file in file_list:
    if file[-3:] == 'png':
        print(file)
