#This python program adds and delete data to the list

number_list = [58,65,37,2098,565,13]

string_list = ["Turku", "Christmas","Happy", "Holidays", "Free", "Choices"]

print(number_list)

print(string_list)

number_list.append(1000)# This line adds the value to the number list
number_list.append(5) # This line adds the value to the number list
string_list.append("Honey")# This line adds the value to the string list
string_list.append("Friend")# This line adds the value to the string list

print(number_list)

print(string_list)

number_list.pop(2) # This line deletes the 3rd value as 2(while indexing from 0)
number_list.append(33)# This line adds the new value to the numberlist
string_list.pop(4) # This line deletes the 5th value as 4(while indexing from 0)
string_list.append("Sugar")# This line adds the new value to the alphabet list

print(number_list)

print(string_list)



