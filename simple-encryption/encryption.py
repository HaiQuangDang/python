import string
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)

def encrypt():
    plain_text = input("Please enter a message to encrypt: ")
    cypher_text = ""
    for character in plain_text:
        index = chars.index(character)
        cypher_text += keys[index]
    print(f"Original message: {plain_text}")
    print(f"Encrypted message: {cypher_text}")


def decrypt():
    cypher_text = input("Please enter a message to decrypt: ")
    decrypted_text = ""
    for character in cypher_text:
        index = keys.index(character)
        decrypted_text += chars[index]
    print(f"Encrypted message: {cypher_text}")
    print(f"Decrypted message: {decrypted_text}")


encrypt()
decrypt()