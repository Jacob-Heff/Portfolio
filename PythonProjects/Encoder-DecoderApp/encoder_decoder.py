import random

def encode(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans, n

def decode(phrase):
    letters = "abcdefghijklmnopqrstuvwxyz"
    x = 0
    while x < 26:
        x = x + 1
        stringtodecrypt=phrase.lower()
        ciphershift=int(x)
        stringdecrypted=""
        for character in stringtodecrypt:
            position = letters.find(character)
            newposition = position-ciphershift
            if character in letters:
                stringdecrypted = stringdecrypted + letters[newposition]
            else:
                stringdecrypted = stringdecrypted + character
        print("You used a cipher shift of ", ciphershift)
        print("Your decrypted message reads:")
        print(stringdecrypted)
        print("\n")

print("Ceaser Cipher Encoder/Decoder")
fb = input("Encode, Decode or End: ")
while True:
    if fb.lower() == "encode":
        phrase = input("Text to encode: ")
        num = random.randint(1, 26)
        encoded, key = encode(phrase, num)
        break
    if fb.lower() == "decode":
        pass    
    if fb.lower() == "end":
        
        quit()
    else:
        fb = input("Encode, Decode or End: ")
    
print(encoded)
decoded = decode(encoded)
print(decoded)