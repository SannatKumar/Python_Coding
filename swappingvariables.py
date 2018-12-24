#This program helps to swap the variables

x= float(input('Enter the X: '))
y= float(input('Enter the Y: '))

temp = x
x = y
y = temp

print('The value of x and y after swapping is {0} and {1} respectively'.format(x,y))
