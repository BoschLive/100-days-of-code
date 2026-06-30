import random

lower_alpha = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']

upper_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

letters = [lower_alpha, upper_alpha]

num_letters = int(input("How many letters would you like in your password? \n"))
num_symbols = int(input("How many symbols would you like in your password? \n"))
num_numbers = int(input("How many numbers would you like in your password? \n"))
length = num_symbols + num_letters
password = []

for n in range(0, num_letters):
    password.insert(random.randint(0, password.__len__()), letters[random.randint(0,1)][random.randint(0,25)])

for n in range(0, num_symbols):
    password.insert(random.randint(0, password.__len__()), symbols[random.randint(0,9)])

for n in range(0, num_numbers):
    password.insert(random.randint(0, password.__len__()), numbers[random.randint(0,9)])

result = ""
for n in password:
    result += n

print(f"Your new password is {result} ")




