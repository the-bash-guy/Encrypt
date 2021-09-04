import os

def encrypt():
    from cryptography.fernet import Fernet
    import easygui
    import time

    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    files = easygui.fileopenbox()

    with open(files, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(files, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    print("DONE ! ! !")
    time.sleep(3)
    os.system("cls")
    import keygen as key
    key.menu()
