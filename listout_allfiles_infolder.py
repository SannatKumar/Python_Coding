#This program list all the files in the directory

# In my case I have forgot to put author name

import os

path = '.'

mypython_files = os.listdir(path)
for name in mypython_files:
    print(name)


    



