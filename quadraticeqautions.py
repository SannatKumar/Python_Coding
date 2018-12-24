#solve the quadratic equation ax2+bx +c =0

#import math module

import cmath

a = float(input('Enter the a: '))
b= float(input('Enter the b: '))
c= float(input('Enter the c: '))

d= (b**2) - (4*a*c)

#Now find two solutions

solution1= (-b-cmath.sqrt(d))/(2*a)
solution2= (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(solution1,solution2))


