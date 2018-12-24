#how to push your existing codes to github creating a new repository

First create a new repository in the Github Account.

Repository Name: Python_Coding

HTTPs: https://github.com/SannatKumar/Python_Coding.git

SSH: git@github.com:SannatKumar/Python_Coding.git

Initialized without README, LICENSE and .gitignore #We ca create them later

Open terminal in your local Folder

Then,

#Initialize git in your local repo

git init

#Check the status every now and then

git status

#Add them to your repo stages them for next step

git add .

#Commit with your first messages

git commit -m "Basics of Python Learning"

#Then copy the HTTPs address from the above and add remote with the url

git remote add origin https://github.com/SannatKumar/Python_Coding.git


#Then push it to the origin

git push origin master

#prompt for git username and Password

Enter the git username and password

#Then its done. You should be able to see your files and folders in the remote repo.

git status










 


