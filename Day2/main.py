#################################################
##          TIP TOTAL CALCULATOR               ##
## Given a combination of options from the     ##
## user, provide an amount for each member of  ##
## a party to pay to split bill equally        ##
#################################################

print("Welcome to the Tip Calculator!")

total = float(input("What was the final bill? "))
percent = int(input("How much would you like to tip? %"))
party_size = int(input("How many people are splitting the bill? "))

tip_amount = total * (percent / 100)

total_per = (total + tip_amount) / party_size

print(f"Each member of your party should pay ${round(total_per, 2)} ")
