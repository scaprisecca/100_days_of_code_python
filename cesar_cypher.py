#!/usr/bin/env python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Ask the user what they want to do - encode or decode
encrypt_or_decrypt = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

# Function for encoding the text
def encrypt(text, shift):
    # take the text and shift each letter the shift_number in the alphabet
    encrypted_message = ""

    for letter in text:
        alphabet_index = alphabet.index(letter)
        new_position = alphabet_index + shift
        new_letter = alphabet[new_position]
        encrypted_message += new_letter

    print(f"The encoded text is {encrypted_message}")

# Function to decode the text
def decrypt(text,shift):
    decrypted_message = ""

    for letter in text:
        new_position = alphabet.index(letter) - shift
        new_letter = alphabet[new_position]
        decrypted_message += new_letter

    print(decrypted_message)

# Determine which function to use based on the user's direction
if encrypt_or_decrypt == 'encode':
    message = input("Type your message:\n").lower()
    shift_number = int(input("Enter your shift number:\n"))

    encrypt(message, shift_number)
elif encrypt_or_decrypt == 'decode':
    decrypt(message, shift_number)
else:
    print("Please choose to 'encode' or 'decode'.")
