# CryptAnalysis for Caesar Encryption
# cipherText = input("Enter the cipher text: ")
# cipherText = cipherText.lower()
# for i in range(1, 26):
#     plainText = ""
#     for c in cipherText:
#         if(c != ' '):
#             plainText += chr((ord(c) - ord('a') + i) % 26 + ord('a'))
#         else:
#             plainText += ' '
#     if(plainText == "easy to break"):
#         print("The key is: ", i)
#     print(plainText, end='\n ---------------------------- \n')

# CryptAnalysis for MonoAlphabetic Encryption
# cipherText = input("Enter the cipher text: ")
# cipherText = cipherText.lower()
# plainText = ""
# for c in cipherText:
#     if c == 'p':
#         plainText += 'e'
#     elif c == 'z':
#         plainText += 't'
#     elif c == 'w':
#         plainText += 'h'
#     else:
#         plainText += c
# print(plainText)

# 2- PolyAlphabetic Encryption
# 2.1- Vigenere Cipher
# reading the inputs
# plainText = input("Enter the plain text: ")
# plainText = plainText.lower()
# key = input("Enter the key: ")
# key = key.lower()

# # preproccesing the key, in order to make it in the same length of the plainText
# while len(key) < len(plainText):
#     key += key

# if len(key) > len(plainText):
#     # this is how we can use slicing in order to remove some characters.
#     key = key[:len(plainText)]


# # preproccesing the 2d array
# alphabets2DMat = []
# for i in range(26):
#     alphabets2DMat.append([])
#     for j in range(26):
#         alphabets2DMat[i].append(chr((i + j) % 26 + ord('a')))

# cipherText = ""
# for i in range(0, len(plainText)):
#     cipherText += alphabets2DMat[ord(plainText[i]) -
#                                  ord('a')][ord(key[i]) - ord('a')]

# print(cipherText)
# cipherText = cipherText.upper()
# assert cipherText == "ZICVTWQNGRZGVTWAVZHCQYGLMGJ"

# # for decryption we just move in the reverse direction
# plainText = ""
# cipherText = cipherText.lower()
# for i in range(0, len(cipherText)):
#     # storing the position of the key in the columns
#     pos = ord(key[i]) - ord('a')
#     for j in range(0, 26):  # iterating till finding this letter
#         if alphabets2DMat[j][pos] == cipherText[i]:
#             # adding the corespoinding letter to the plainText.
#             plainText += chr(j + ord('a'))
#             break
# print(plainText)
# assert plainText == "wearediscoveredsaveyourself"

# 2.2- Autokey Cipher
# plainText = input("Enter the plain text: ")
# plainText = plainText.lower()
# key = input("Enter the key: ")
# key = key.lower()

# # generation of the keyStream
# keyStream = key + plainText
# keyStream = keyStream[: len(plainText)]
# assert keyStream == "deceptivewearediscoveredsav"


# # applying the encryption
# cipherText = ""
# for i in range(0, len(plainText)):
#     # 2 34an el mfrod atr7 el ord bta3 el a mn kol wahda 34an lama agy a3ml el mod yetl3 el equation mzbota
# cipherText += chr(((ord(plainText[i]) +
#                     ord(keyStream[i])) - (2 * ord('a'))) % 26 + ord('a'))

# cipherText = cipherText.upper()
# print(cipherText)
# assert cipherText == "ZICVTWQNGKZEIIGASXSTSLVVWLA"

# 3- Vername Cipher
# import random
# import string

# plainText = input("Enter the plain text: ")
# plainText = plainText.lower()


# # generating a random keystream of the same length of the plainText
# keyStream = ''.join(random.choice(string.ascii_lowercase)
#                     for i in range(len(plainText)))
# assert len(keyStream) == len(plainText)

# # applying the encryption
# cipherText = ""
# for i in range(0, len(plainText)):
#     cipherText += chr(((ord(plainText[i]) +
#                         ord(keyStream[i])) - (2 * ord('a'))) % 26 + ord('a'))

# cipherText = cipherText.upper()
# print(cipherText)

