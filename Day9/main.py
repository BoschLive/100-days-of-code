
dictionary = {}

#When program runs, for looking pretty
print('\n'*80)
print('''                         ___________
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                   jgs/_______________\\''')

choice = ''
while choice != 'n':
    name = input("What is your name?\n")
    bet = int(input("Enter an amount to bid.\n"))

    dictionary[name] = bet

    # loop for input validation on y/n choice to continue betting
    while True:
        choice = input("\nAre there more bids to be placed? [y]es or [n]o\n")
        if choice == 'n':
            break
        elif choice != 'y':
            print("Invalid input")
        else:
            print('\n'*80)
            break

# find highest value in dict and record the associated key
tempValue = 0
for key in dictionary:
    if dictionary[key] > tempValue:
        highest_bid = dictionary[key]
        tempValue = dictionary[key]
        winner = key

print(f'\nThe winner is {winner}! They bid ${highest_bid}!\n')

