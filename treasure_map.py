# Defining our rows
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

# Creating the map
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
# Getting the positions from the user
position = input("Where do you want to put the treasure? ")

# getting the column
column = int(position[0]) - 1

# getting the row
row = int(position[1]) - 1

# Modifying the selected coordenate
map[row][column] = 'X'

# Printing the result
print(f"{row1}\n{row2}\n{row3}")
