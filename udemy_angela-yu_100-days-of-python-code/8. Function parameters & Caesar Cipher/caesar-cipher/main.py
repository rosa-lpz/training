
import string
string.ascii_lowercase

# List of letters
# alphabet=list(string.ascii_lowercase)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd',
               'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input ("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text =input("Type your message:\n").lower()
shift =int(input("Type the shift number: "))

# 1. Create function "encrypt" that takes the "text and "shift" as inputs

def encrypt(plain_text, shift_amount):
    """2. Insider the "encrypt" function" - Shift each letter of the 'text' forwards in the alphabet by the shif
    amount and print the encrypted text
    e.g. 1
    plain_text="hello", shift =5
    chipher_text="mjqqt"
    print output:"The encoded text is mjqqt"

    e.g. 2
    plain_text="zulu", shift =5
    chipher_text="ezqz"
    print output:"The encoded text is ezqz"
    """

    # using index method (for lists) and for loop
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    """2. Insider the "decode" function" - Shift each letter of the 'text' *backwards 
    in the alphabet by the shift amount and print the decrypted text
    e.g. 1
    cipher_text="mjqqt", shift =5
    plain_text="hello"
    print output:"The decoded text is hello"

    e.g. 2
    chipher_text="ezqz",shift =5
    plain_text="zulu" 
    print output:"The decoded text is zulu"
    """

    # using index method (for lists) and for loop
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decoded text is {plain_text}")

# 3. Call the encrypt function
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)