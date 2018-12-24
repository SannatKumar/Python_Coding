"""
Title: Python file handling
Author: Raj Kumar Tiwari
Date: Dec 11, 2018
Description: This program appends something('the text you give') to the file in the same directory
"""
f=open('filehandlingpy.txt', 'a') #if there is no such file then it will create it.
f.write('\n' + 'This is the appendix')
f.close()
