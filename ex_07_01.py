# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:00:37 2020

@author: morri
"""

# 7.1 Write a program that prompts for a file name, then 
    # opens that file and reads through the file, and 
    # print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.
# Use words.txt as the file name

fname = input('Enter file name: ')
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)