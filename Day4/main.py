################################################
##            ROCK PAPER SCISSORS             ##
##  Take an input from the user and compare   ##
##  it to randomly generated "choice" for the ##
##  opponent. Compare choices using standard  ##
##  Rock, Paper, Scissors rules.              ##
################################################
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
---'    ____)____
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

art = [rock, paper, scissors]
options = ["ROCK", "PAPER", "SCISSORS"]

print("WELCOME TO ROCK PAPER SCISSORS")
choice = int(input("Choose an option: 0 for rock, 1 for paper, 2 for scissors "))

print(f"You chose: {options[choice]}")
print(art[choice])

cpu_choice = random.randint(0,2)

print(f"The computer chose: {options[cpu_choice]}")
print(art[cpu_choice])

#Set conditions for win states and draw, assume all other possibility is a loss
if (cpu_choice == 0 and choice == 1) or (cpu_choice == 1 and choice == 2)  or (cpu_choice == 2 and choice == 0):
    print("YOU WIN!")
elif cpu_choice == choice:
    print("IT'S A DRAW!")
else:
    print("YOU LOSE!")