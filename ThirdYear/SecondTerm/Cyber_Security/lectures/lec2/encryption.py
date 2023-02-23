cipherText = input("Enter the cipher text: ")
cipherText = cipherText.lower()
for i in range(1, 26):
    plainText = ""
    for c in cipherText:
        if(c != ' '):
            plainText += chr((ord(c) - ord('a') + i) % 26 + ord('a'))
        else:
            plainText += ' '
    if(plainText == "easy to break"):
        print("The key is: ", i)
    print(plainText, end='\n ---------------------------- \n')
