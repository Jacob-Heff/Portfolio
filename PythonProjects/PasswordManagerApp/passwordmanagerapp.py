# Jacob Heffington
# Password Manager
# Resource: github.com/techwithtim/5-Python-Projects-For-Beginners

from cryptography.fernet import Fernet
import PySimpleGUI as sg

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def key_window():
    # All the stuff inside your window.
    layout = [  [sg.Text("Key not found! Creating Key! Please run again!")],
                [sg.Button('Ok')] ]

    # Create the Window
    window = sg.Window('Key Not Found', layout)

    # Event Loop to process "events"
    while True:
        event, values = window.read()

        # if user closes window or clicks ok
        if event == sg.WIN_CLOSED or event == 'Ok':
            break

    window.close()

def key_check():
    try:
        file = open('key.key', 'r')
        file.read()
        file.close()
    except FileNotFoundError:
        write_key()
        key_window()
        quit()

def mstr_pass_window():
    # All the stuff inside your window.
    layout = [  [sg.Text("Create a Master Password")],
                [sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Master Password', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        return values[0]

    window.close()

def mstr_pass(fer):
    mst_pwd = mstr_pass_window()
    test = input("Create a Master Password: ")
    print(type(mst_pwd))
    print(type(test))
    with open('passwords.txt', 'wb') as f:
        f.write("Password Manager" + "|" + fer.encrypt(mst_pwd.encode()).decode() + "\n")

def main():
    key_check()
    key = load_key()
    fer = Fernet(key)
    mstr_pass(fer)

if __name__ == "__main__":
    main()