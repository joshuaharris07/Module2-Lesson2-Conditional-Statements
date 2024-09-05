#Leap Year Explorer

#Task 1: Leap Year Checker 
# Write a Python program that prompts the user to input a year. 
# The program should determine if the given year is a leap year or not and then display an appropriate message. 
# Please note that this is the definition of a leap year: 
# Every year that is exactly divisible by four is a leap year, 
# except for years that are exactly divisible by 100, 
# but these centurial years are leap years if they are exactly divisible by 400.

is_leap = False
year = int(input("Please input a year to check if it is a leap year: "))

if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True

if is_leap:
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year.")