# Importing the random module in order to use it
import random

# Importing what I need from my custom module
from my_module import pi

# Generates a random integer, including the specified numbers
random_integer = random.randint(100, 200)
print(random_integer)


# Generating a random float number with the random method
# this generates a random number between 0.0 and 1.0 not inclusive
random_float = random.random()
print(random_float)


# Generating a random number between specified numbers
random_number = random.randrange(1,5)
print(random_number)


print(pi)