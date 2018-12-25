# This program helps to make use of if, elif, else

print("Travel to Helsinki: ")
print("Please Select your Choice of transportation: ")
print("A for Aeroplane\n")
print("B for Onni Bus\n")
print("C for Car\n")
print("H for Hitchhiking\n")
print("T for Taxi\n")
print("R for Rail or Rauta\n")

customer_choice = input()

if customer_choice == 'A' or customer_choice == 'a':
   print("Take 1 number bus from Turku Center to Airport and buy a ticket from airport\n")
   print("Time Taken : 50 minutes\n")
elif customer_choice == 'B' or customer_choice == 'b':
   print("Visit the Onnibus site and buy a ticket. Then the stops are at Aurakatu and Hameenkatu\n")
   print("Time Taken : 2 hours\n")
elif customer_choice == 'C' or customer_choice == 'c':  
   print("Visit the Turku Fleamarket page if there is someone posting a free ride to helsinki\n")
   print("Time Taken : 2 hours or depends\n")
elif customer_choice == 'H' or customer_choice == 'h':
   print("You need to hold a playcard and stay on the shoulder of Helsinki highway.\n")
   print("Time Taken : Days\n")
elif customer_choice == 'T' or customer_choice == 't':
   print("Taxi are widely available but maybe expensive\n")
   print("Time Taken : 1 hour 45 minutes\n")
elif customer_choice == 'R' or customer_choice == 'r':
   print("Visit the Trainstation and buy a ticket\n")
   print("Time Taken : 2 Hours\n")
else:
   print("No Such options available. You might have to walk and it takes too long")
