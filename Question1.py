# Decisions at the Crossroad

#Task 1: Code Correction 
# You are provided with a Python script that uses conditional statements to tell if a number is positive, negative, or zero. 
# But it has some errors. Identify and fix them.

number = float(input("Enter a number: ")) #converting to a float to account for any decimals the user enters.

if number > 0:
    print("The number is positive.")
elif number == 0:                         #added a =
    print("The number is zero.")
else:                                     #else can't take any conditions.
    print("The number is negative.")