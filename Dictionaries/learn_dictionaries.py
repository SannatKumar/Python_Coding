""" This program initiates the dictionary, prints(individual & single), 
appends and replace new data and creates new field, prints the length of
 the dictionary and deletes the field also """ 

#our Dictionary initiated with constant values

our_dictionary = {'Name': 'RajKumar', 'Country' : 'Nepal', 'Favourite_numbers':[7, 19, 199]}

#This prints everthing inside the dictionary
print(our_dictionary)

#Print single data name

print(our_dictionary['Name'])
print(our_dictionary['Country'])
print(our_dictionary['Favourite_numbers'])


# Append something new to the dictionary

our_dictionary['Favourite_language'] = 'Japanese'

our_dictionary['Country'] = 'finland' # Here it removes Nepal and replace finland with it.

our_dictionary['Favourite_numbers'] = 565 # This would replace previous all values with this input

print(our_dictionary)

# Delete something from the dictionary

our_dictionary.pop('Favourite_numbers')

our_dictionary.pop('Country') # Here it removes country

print(our_dictionary)

dictionary_length = len(our_dictionary)

print("The dictionary Length is ",format(dictionary_length))# This will print the length of the dictionary
