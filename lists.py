# Lists in python

# Declaring a list
states = ["Washington", "New York", "Delaware", "Pennsylvania"]
# the order of the items in the list is important


# reading the first state by adding an index or position
print(states[0])


# reading with a negative index will start at the end of the list
print(states[-1])


# changing the list in the specified position
states[0] = "North Carolina"
print(states)


# adding an item to the end of the list
states.append("Montana")
print(states)


# extending the current list with another list, 
# just like append but with multiple items
states.extend(["Oklahoma", "New Mexico"])
print(states)


