"""
Title: Python File handling
Author: Raj Kumar Tiwari
Date: Dec 11, 2018
Description: This program file reads the file and prints the message in the same directory
"""
f=open('filehandlingpy.txt', 'r')
message=f.read()
print(message)
f.close
