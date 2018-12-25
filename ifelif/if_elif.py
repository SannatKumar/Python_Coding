# This program make uses of the if elif 
"""
name = input("Enter your name: ")

if name == 'rajkumar':
    print("HI Raj Kumar")
elif name == 'deepak':
    print("Hi Deepak")
elif name == 'Python':
    print("HI! Lovely Language Python")
else:
    print("!!! HI !!!! Anynomous !!!")


"""

name = input("Enter your name: ")

if name == 'rajkumar' or name == 'RAJKUMAR' or name == 'Rajkumar':
    print("HI Raj Kumar")
elif name == 'deepak' or name == 'DEEPAK' or name == 'Deepak':
    print("Hi Deepak")
elif name == 'Python' or name == 'PYTHON' or name == 'python':
    print("HI! Lovely Language Python")
else:
    print("!!! HI !!!! Anynomous !!!")
