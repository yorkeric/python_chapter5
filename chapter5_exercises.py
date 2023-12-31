# ----------------------------------------------
# Algorithm Workbench
# ----------------------------------------------
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

# ----------------------------------------------
# Programming Exercises
# ----------------------------------------------
# Question 1 - Kilometer Converter
# Write program that accepts distance (in kilometers)
# Converts from kilometers to miles
# Prompt for the distance in kilometers 
# Write function that accepts the input of kilometers and returns the miles 
# Call function to convert to miles
# Print the total miles
def convert_to_miles(kilometers):
    return kilometers * .6214
kilometers = int(input("Enter distance in kilometers: "))
miles = convert_to_miles(kilometers)
print("Total miles:", miles)

# Question 7 - Stadium Seating
# Write a program that calcuates the income generated from ticket sales
# Prompt for the number of tickets sold for Class A, Class B, and Class C
# Write a function for each ticket class that will prompt for tickets sold and return the total amount
# Calculate total by adding each total amount per class
# Print will call each function, add the total amount per class, and display a message with the total
def get_class_a_total_sales():
    return int(input("Class A tickets sold: ")) * 20
def get_class_b_total_sales():
    return int(input("Class B tickets sold: ")) * 15
def get_class_c_total_sales():
    return int(input("Class C tickets sold: ")) * 10
print("Total income in ticket sales:", get_class_a_total_sales() + get_class_b_total_sales() + get_class_c_total_sales())

# Question 17 - Prime Numbers
# Calculate if input number is prime or not prime
# Prime numbers are only evenly divisible by itself and 0
# Loop through the range starting at 2 and for each number in the range check if divisble by that number
# If any of the numbers in that range are divisible by that number, then stop checking as the number is prime
# Print a statment if the number is prime or not
# Check if number is 1 and return is not prime
def is_prime(num):
    if(num == 1):
        return False
    else:
        for i in range(2, num):
             if(num % i) == 0:
                return False
        return True
input_number = int(input("Enter number to check if prime: "))
if(is_prime(input_number)):
    print("The number is prime")
else: 
    print("The number is not prime")
    
# Question 18 - Prime Number List
# Using the is_prime function, print out all the prime numbers from 1 to 100
# Loop over the range, check the function, and print the number if is prime 
def is_prime(num):
    if(num == 1):
        return False
    else:
        for i in range(2, num):
             if(num % i) == 0:
                return False
        return True
print("All the numbers from 1 to 100 that are prime:")
for i in range(1, 101):
    if(is_prime(i)):
        print(i)