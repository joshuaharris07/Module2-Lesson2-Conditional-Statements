#The Greatest Showdown

#Task 1: Identify the Greatest 
# Write a Python program that asks the user to enter three numbers. 
# Your code should then identify and print out the largest number among the three.


num1 = int(input("We will have you enter 3 numbers for comparison. Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

largest_num = num1

if num2 > largest_num:
    largest_num = num2
if num3 > largest_num:
    largest_num = num3

print(f"The largest number is {largest_num}!")


#Task 2: Identify the Smallest 
# Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

num1 = int(input("We will have you enter 3 numbers for comparison. Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

largest_num = num1
smallest_num = num1

if num2 > largest_num: #if num2 is bigger than num1, it is the biggest sofar
    largest_num = num2
else:                  #if num2 isn't bigger, then it is automatically the smallest so far
    smallest_num = num2

if num3 > largest_num:
    largest_num = num3
elif num3 < smallest_num:
    smallest_num = num3

print(f"The largest number is {largest_num}, and the smallest number is {smallest_num}!")