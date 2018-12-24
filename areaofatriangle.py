#This program helps to print area of the triangle

a = float(input('Enter one of the side: '))
b= float(input('Enter another side: '))
c = float(input('Enter the remaining side: '))

# Here comes the formula to calculate the area of the triangle

#calculate the semi perimeter

s =float((a + b + c) / 2)

#Now calculate the area

area =float((s*(s-a)*(s-b)*(s-c)) **0.5)

print('The area of the triangle is %0.2f'%area)


