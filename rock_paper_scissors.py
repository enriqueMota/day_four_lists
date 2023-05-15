import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.choice([0, 1, 2])
graphic_board = f"{choices[user_choice]}\nComputer chose:\n{choices[computer_choice]}\n"
winner = "You lose"

if user_choice == computer_choice:
    winner = "It's a draw"
    print(graphic_board)
    print(winner)
elif (
    (user_choice == 0 and computer_choice == 2) or
    (user_choice == 1 and computer_choice == 0) or
    (user_choice == 2 and computer_choice == 1)
):
    winner = "You win!"
    print(graphic_board)
    print(winner)
else:
    print(graphic_board)
    print(winner)
