# Algorithm Workbench

# Question 1
# Write a function that accepts an argument and displays the argument multiplied by 10
# delclar a function named times_ten and add print statment to display result
# call function to display the result
# 10 x 10 = 100
def times_ten(num):
    print(str(num) + " x 10 =", (num * 10))
times_ten(10)

# Question 6
# Write a statement that generates a randome number between 1 and 100
# Assign to variable named rand
# Print the value of rand
import random
rand = random.randint(1, 100)
print(rand)

# Programming Exercises

# Question 1 - Kilometer Converter
# Write program that accepts distance (in kilometers)
# Converts from kilometers to miles
def convert_to_miles(kilometers):
    return kilometers * .6214
kilometers = int(input("Enter distance in kilometers: "))