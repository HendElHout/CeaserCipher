letters = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(plaintext, key):
    ciphertext = ''  # Use an empty string for concatenation
    for letter in plaintext:
        letter = letter.lower()
        if letter.isalpha():  # Check if it's a letter from a to z
            index = letters.find(letter)
            if index != -1:
                new_index = (index + key) % 26  # Use modulo for wrapping
                ciphertext += letters[new_index]
        else:
            ciphertext += letter  # Preserve non-alphabetic characters

    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if letter.isalpha():
            index = letters.find(letter)
            if index != -1:
                new_index = (index - key) % 26
                plaintext += letters[new_index]
        else:
            plaintext += letter

    return plaintext


print()
print('---CEASER CIPHER---')
print()
print('Do You Want Encryption or Decryption?')
user_input = input('e/d: ').lower()

if user_input == 'e':
    print('You chose encryption')
    print()
    key = int(input('Enter the Key (1 through 26): '))
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt(text, key)
    print(f'CipherText: {ciphertext}')

elif user_input == 'd':
    print('You chose decryption')
    print()
    key = int(input('Enter the Key (1 through 26): '))
    text = input('Enter the text to decrypt: ')
    plaintext = decrypt(text, key)
    print(f'PlainText: {plaintext}')

else:
    print("Invalid input. Please enter 'e' for encryption or 'd' for decryption.")