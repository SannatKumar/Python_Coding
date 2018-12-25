# This function takes parameter and gives the result accordingly

choice_date = input("Enter the date(Year.month.date) format: ")
year, month, day = map(int, choice_date.split('.'))

if year<1900 or year > 2018:
    print("Invalid Year")
elif month < 1 or month > 12:
    print("Invalid Month")
elif day <1 or day > 32:
    print ("Invalid Date")

def display(month):
    if month == 1 :
        print("English: January")
        print("Finnish: Tammikuu")
    elif month == 2 :
        print("English: February")
        print("Finnish: Helmikuu")
    elif month == 3:  
        print("English: March")
        print("Finnish: Maaliskuu")
    elif month == 4:
        print("English: April")
        print("Finnish: Huhtikuu")
    elif month == 5:
        print("English: May")
        print("Finnish: Toukokuu")
    elif month == 6:
        print("English: June")
        print("Finnish: Kesäkuu")
    elif month == 7:
        print("English: July")
        print("Finnish: Heinäkuu")
    elif month == 8:
        print("English: August")
        print("Finnish: Elokuu")
    elif month == 9:
        print("English: September")
        print("Finnish: Syyskuu")
    elif month == 10:
        print("English: October")
        print("Finnish: Lokakuu")
    elif month == 11:
        print("English: November")
        print("Finnish: Marraskuu")
    elif month == 12:
        print("English: December")
        print("Finnish: Joulukuu")
    else:
        print("No Such options available on months")

display(month)
