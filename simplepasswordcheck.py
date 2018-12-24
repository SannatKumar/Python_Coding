# this program simply checks the password prints the output

passwordFile =open('/usr/Documents/python/password.txt')
secretPassword = passwordFile.read()
typedPassword = input('Enter your password: ')
if typedPassword == secretPassword:
	print('Access granted')
	if typedPassword == '12345':
		print('That password is one that an idiot puts on their luggage.')
else:
	print('Access denied') 

