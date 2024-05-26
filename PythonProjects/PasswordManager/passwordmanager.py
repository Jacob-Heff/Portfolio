# Jacob Heffington
# Password Manager
# Resource: github.com/techwithtim/5-Python-Projects-For-Beginners

from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

try:
    file = open('key.key', 'r')
    file.read()
    file.close()
except FileNotFoundError:
    print("Key not found! Creating Key! Please run again!")
    write_key()
    quit()

key = load_key()
fer = Fernet(key)

def mstr_pass():
    mst_pwd = input("Create a Master Password: ")

    with open('passwords.txt', 'wb') as f:
        f.write("Password Manager" + "|" + fer.encrypt(mst_pwd.decode()).encode() + "\n")

def check_mstr_pass(mstrpass):
    with open('passwords.txt', 'rb') as f:
        data = f.readline().rstrip()
        name, passw = data.split("|")
        read_passw = fer.decrypt(passw.encode()).decode()
        if read_passw != mstrpass:
            quit()    

try:
    file = open('passwords.txt', 'r')
    file.read()
    file.close()
except FileNotFoundError:
    print("Master Password not found! Please create a Master Password and run again!")
    mstr_pass()
    quit()
    
mstr_pwd = input("Please provide the master password: ") 
check_mstr_pass(mstr_pwd)

def view():
    with open('passwords.txt', 'r') as f:
        next(f)
        for line in f.readlines():
            data = line.rstrip()
            name, passw = data.split("|")
            print("Name:", name + " | Password:", fer.decrypt(passw.encode()).decode())
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view/add), enter q to quit: ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue