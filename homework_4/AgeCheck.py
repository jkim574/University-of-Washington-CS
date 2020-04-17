# This program prompts you for the current date
# and several birthdates.
# It computes the age in years of the youngest
# person and wishes Happy Birthday as appropriate.

# Minimum allowed age? 21
# Current year? 2009
# Current month? 4
# Current day? 28
# Number of people? 3

# Birth year? 1988
# Birth month? 4
# Birth day of month? 29

# Birth year? 1986
# Birth month? 4
# Birth day of month? 28
# Happy 23rd birthday!

# Birth year? 1985
# Birth month? 1
# Birth day of month? 1

# The youngest person is age 20
# Sorry, you have not all reached your 21st birthday.





# This program prompts you for the current date
# and several birthdates.
# It computes the age in years of the youngest
# person and wishes Happy Birthday as appropriate.

# Minimum allowed age? 10
# Current year? 2010
# Current month? 2
# Current day? 28
# Number of people? 2

# Birth year? 1970
# Birth month? 2
# Birth day of month? 28
# Happy 40th birthday!

# Birth year? 1999
# Birth month? 12
# Birth day of month? 31

# The youngest person is age 10
# Everyone is old enough.  Welcome!







# This program prompts you for the current date
# and several birthdates.
# It computes the age in years of the youngest
# person and wishes Happy Birthday as appropriate.

# Minimum allowed age? 5
# Current year? 2009
# Current month? 4
# Current day? 28
# Number of people? 3

# Birth year? 2009
# Birth month? 4
# Birth day of month? 28
# Happy 0th birthday!

# Birth year? 2007
# Birth month? 4
# Birth day of month? 28
# Happy 2nd birthday!

# Birth year? 2005
# Birth month? 4
# Birth day of month? 28
# Happy 4th birthday!

# The youngest person is age 0
# Sorry, you have not all reached your 5th birthday.


from math import *


def introduction():
    print("This program prompts you for the current data \nand several birthdates.")
    print("It computes the age in years of the youngest \nperson and wishes Happy Birthday as appropriate.")


#prompts user to input the current year, and number of people.
def age():
    min_allow_age = int(input("Minimum allowed age? "))
    current_year = int(input("Current year? "))
    current_month = int(input("Current month? "))
    current_day = int(input("Current day? "))
    print()

    ages = []
    num = int(input("Number of people? "))
    for each_person in range(num):
        #each person has his/her own birth year, month, and date data.
        birth_years = int(input("Birth year? "))

        current_age = current_year - birth_years
        ages.append(current_age)

        birth_month = int(input("Birth month? "))
        birth_day = int(input("Birth day of month? "))
        if birth_month == current_month and birth_day == current_day:
            print("Happy", ordinal(current_age), "birthday!")
        print("")

    print("The youngest person is age", str(min(ages)))
    if min_allow_age <= current_age:
        print("Everyone is old enough. Welcome!")
    else:
        print("Sorry, you have not all reached your", ordinal(min_allow_age), "birthday!")





#this method prints an ordinal number and adds suffix.
SUFFIXES = {1: 'st', 2:'nd', 3:'rd'}
def ordinal(number):
    #checking for 10~20 since these numbers don't follow the normal counting style
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        suffix = SUFFIXES.get(number % 10, 'th')
    return str(number) + suffix



if __name__ == "__main__":
    introduction()
    print()
    age()
