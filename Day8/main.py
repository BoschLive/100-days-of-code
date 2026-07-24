#############################################
##              CAESAR CIPHER              ##
#############################################


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

def encrypt(shift, plaintext):
    ciphertext = ""

    for letter in plaintext:

        if letter.lower() in alphabet:
            x = alphabet.index(letter.lower())
            position = (x + shift) % 26
            if letter.isupper():
                ciphertext += (alphabet[position].upper())
            else:
                ciphertext += (alphabet[position])
        else:
            ciphertext += letter
    return ciphertext

def decrypt(shift, ciphertext):
    plaintext = ""

    for letter in ciphertext:

        if letter.lower() in alphabet:
            x = alphabet.index(letter.lower())
            position = (x - shift) % 26
            if letter.isupper():
                plaintext += (alphabet[position].upper())
            else:
                plaintext += (alphabet[position])
        else:
            plaintext += letter
    return plaintext


def main():
    loop = 'y'

    while loop == 'y':
        state = input("Do you wish to encrypt or decrypt? (type 'encrypt' or 'decrypt')\n ")
        text = input("Enter your text: ")
        shift = int(input("\nEnter the amount to shift: "))

        if state == 'encrypt':
            product = encrypt(shift=shift, plaintext=text)
        elif state == 'decrypt':
            product = decrypt(shift=shift, ciphertext=text)
        else:
            print("Invalid Options. ")
            return 0

        print(f"Result: {product}")

        loop = input("\nType 'y' to go again or 'n' to stop: ")

    return 0

if __name__ == "__main__":
    main()