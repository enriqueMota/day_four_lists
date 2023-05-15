"""
You are going to write a program that will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.
"""

# Importing the random module here
import random

# Saving all the names as a string
names_string = input("Give me everybody's names, separated by a comma. ")

# Saving all the names in a list
names = names_string.split(", ")

# Choosing a random member of the list by
# generating an index with the random method
chosen_one = random.randint(0, len(names))

# Printing the chosen member to pay the meal
print(f"{names[chosen_one]} is going to buy the meal today!")
