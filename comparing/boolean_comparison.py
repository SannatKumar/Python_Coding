#This program compares values and prints the boolean result

#Boolean refers to the value True or Fale


"""*** Things I learned here.Putting print after input produces "None" prompt word before user gets to input
"""
first_number = input("Enter your first value to compare: ") 
second_number = input("Enter your second value to compare: ")
third_number = input("Enter your third Number: ")
fourth_number = input("Enter your fourth Number: ")

#check greater than is True

boolean_value = first_number > second_number

print(boolean_value)

#check smaller than is True

boolean_value = first_number < second_number

print(boolean_value)

#check less than or equals to True

boolean_value = first_number <= second_number

print(boolean_value)

#check greater than or equals to True

boolean_value = first_number >= second_number

print(boolean_value)

#check if equals to True

boolean_value = first_number == second_number

print(boolean_value)

#check if not equals to True

boolean_value = first_number != second_number

print(boolean_value)


# and opertaor

# This operator gives the result true if both conditions are true

boolean_value = first_number > second_number and third_number > fourth_number

print(boolean_value)


# or opertaor

# This operator gives the result true if only conditions is true

boolean_value = first_number > second_number or third_number > fourth_number

print(boolean_value)


