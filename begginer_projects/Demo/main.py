#Mini projects

#1. Create a greeting for your program.
# print("Welcome to the Band Name Generator")
# #2. Ask the user for the city that they grew up in.
# city = input("What's name of the city you grew up in?\n")
# #3. Ask the user for the name of a pet.
# pet = input("What's name of a pet?\n")
# #4. Combine the name of their city and pet and show them their band name.
# print(city+pet)
# #5. Make sure the input cursor shows on a new line:

# ------------------------------
#2. If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# print("Welcome to the tip calculator.")
# bill = float(input("What was teh total bill?\n"))
# tip = int(input("What percentage tip would you like to give? 10,12, or 15?\n"))
# pers = int(input("How many people to split the bill?\n"))
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / pers
# final_amount = "{:2f}".format(bill_per_person)
# print(f"Each person should pay: ${final_amount}")

#ticket machine
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height?\n"))
#
# if height >= 120:
#     print("You can ride. You can buy a ticket")
#     age = int(input("What is your age?\n"))
#     bill = 0
#     if age < 12:
#         print("Please pay $5")
#         bill = 5
#     elif age <= 18:
#         print("Please pay $8")
#         bill = 8
#     else:
#         print("Please pay $12")
#         bill = 12
#
#     wants_photo = input("Do you want a photo taken? Y or N.")
#     if wants_photo == "Y":
#         bill = bill + 3
#     print(f"Your final bill is ${bill}")
#
# else:
#     print(("you cannot ride. Sorry"))

#TREASURE ISLAND GAME
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# step1 = input("Left or right?\n")
# if(step1.lower() == "right"):
#     print("Game Over")
# else:
#     step2 = input("Swim or wait?\n")
#     if(step2.lower() == "swim"):
#         print("Game Over.")
#     else:
#         step3 = input("Which door? Red, Blue or Yellow?\n")
#         if((step3.lower() == "red") or (step3.lower() == "blue")):
#             print("Game Over.")
#         else:
#             print("You WIN!")

#------------------------------------------------------------------------------------------

#TREASURE MAP
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
#
# letter = position[0].lower()
# abc = ["a","b","c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"
#
# print(f"{line1}\n{line2}\n{line3}")

#-----------------------------------------------------------------------------

#ROCK-PAPER-SCISSORS

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# import random
#
# game_image = [rock, paper, scissors]
#
# user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#
# if user >= 3 and user < 0:
#     print("You typed an invalid number, you lose!")
# else:
#     print(game_image[user])
#
#     computer = random.randint(0, 2)
#     print("Computer chose: ")
#     print(game_image[computer])
#
# if user == 0 and computer == 2:
#     print("YOU WIN!")
# elif computer == 0 and user == 2:
#     print("YOU LOSE!")
# elif computer > user:
#     print("YOU LOSE!")
# elif user > computer:
#     print("YOU WIN")
# elif computer == user:
#     print("It s a draw!")
# else:
#     print("YOU write a invalid number! You lose!")

#-----------------------------------------------------------------------

#PYPASSWORD Generator
import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# password1 = ""
#
# for char in range(1, nr_letters + 1):
#     password1 += random.choice(letters)
#
# for char in range(1, nr_numbers + 1):
#     password1 += random.choice(numbers)
#
# for char in range(1, nr_symbols + 1):
#     password1 += random.choice(symbols)
#
# print(password1)

# password_list = []
# for char in range(1, nr_letters + 1):
#     password_list.append(random.choice(letters))
# for char in range(1, nr_symbols + 1):
#     password_list += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password_list += random.choice(numbers)
#
# random.shuffle(password_list)
#
# password2 = ""
# for char in password_list:
#     password2 += char
# print(password2)

#----------------------------------------------------------------------------------
#HANGMAN
# import random
#
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# word_list = ["ardvark", "baboon", "camel", "live", "play", "alphabeth"]
# chosen_world = random.choice(word_list) #this is how you can choose a random word from the list
# word_lenght = len(chosen_world)
# lives = 6
#
# display = []
# for letter in range(word_lenght):
#     display += "_"
#
# end_of_game = False
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#
#     for position in range(word_lenght):
#         letter = chosen_world[position]
#         if letter == guess:
#             display[position] = letter
#     if guess not in chosen_world:
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You looose!")
#
#     print(f"{' '.join(display)}")
#
#     if "_" not in display:
#         end_of_game = True
#         print("You win!!")
#     print(stages[lives])

