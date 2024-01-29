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
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
step1 = input("Left or right?\n")
if(step1.lower() == "right"):
    print("Game Over")
else:
    step2 = input("Swim or wait?\n")
    if(step2.lower() == "swim"):
        print("Game Over.")
    else:
        step3 = input("Which door? Red, Blue or Yellow?\n")
        if((step3.lower() == "red") or (step3.lower() == "blue")):
            print("Game Over.")
        else:
            print("You WIN!")



