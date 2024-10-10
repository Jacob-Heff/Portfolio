# Vignére cipher encryption/decryption
# 10/8/2024

import string
import tkinter

# Create a Vignére cipher table
alphabet = string.ascii_uppercase
table = []
for i in range(len(alphabet)):
    row = [alphabet[(i + j) % 26] for j in range(len(alphabet))]
    table.append(row)

def main():
    ''' Main Function '''
    def encrypt(plaintext, key):
        '''Encrypt the plaintext using the key'''

        key = key.upper() # Convert the key to uppercase
        plaintext = plaintext.upper() # Convert the plaintext to uppercase
        key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)] # Repeat the key to match the length of the plaintext
        ciphertext = "" # Initialize the ciphertext
        for i in range(len(plaintext)): # Iterate over the plaintext
            if plaintext[i] == " ": # If the character is a space, add a space to the ciphertext and key
                ciphertext += " " # Add a space to the ciphertext
                key = key[:i] + " " + key[i:] # Add a space to the key
            else: # If the character is not a space
                ciphertext += table[ord(key[i]) - 65][ord(plaintext[i]) - 65] # Add the character to the ciphertext
        output["text"] = ciphertext # Display the ciphertext
        
    def decrypt(ciphertext, key):
        '''Decrypt the ciphertext using the key'''

        key = key.upper() # Convert the key to uppercase
        key = key * (len(ciphertext) // len(key)) + key[:len(ciphertext) % len(key)] # Repeat the key to match the length of the ciphertext
        plaintext = "" # Initialize the plaintext
        for i in range(len(ciphertext)): # Iterate over the ciphertext
            if ciphertext[i] == " ": # If the character is a space, add a space to the plaintext and key
                plaintext += " " # Add a space to the plaintext
                key = key[:i] + " " + key[i:] # Add a space to the key
            else: # If the character is not a space
                for j in range(len(alphabet)): # Iterate over the alphabet
                    if table[ord(key[i]) - 65][j] == ciphertext[i]: # If the character is found in the table
                        plaintext += alphabet[j] # Add the character to the plaintext
                        break # Break the loop
        
        output["text"] = plaintext # Display the plaintext

    root = tkinter.Tk()
    root.title("Vignére Cipher")
    root.geometry("300x200")

    # Create a label widget
    label = tkinter.Label(root, text="Enter the plaintext/ciphertext:")
    label.pack()

    # Create an entry widget
    text = tkinter.Entry(root)
    text.pack()

    # Create a label widget
    key_label = tkinter.Label(root, text="Enter the key:")
    key_label.pack()

    # Create an entry widget
    key = tkinter.Entry(root)
    key.pack()

    # Create a button widget
    encrypt_button = tkinter.Button(root, text="Encrypt", command=lambda: encrypt(text.get(), key.get()))
    encrypt_button.pack()

    # Create a button widget
    decrypt_button = tkinter.Button(root, text="Decrypt", command=lambda: decrypt(text.get(), key.get()))
    decrypt_button.pack()

    # Create a label widget
    output = tkinter.Label(root, text="")
    output.pack()

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()