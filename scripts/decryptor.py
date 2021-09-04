import os


def decrypt():
    from cryptography.fernet import Fernet
    import easygui
    import time

    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    files = easygui.fileopenbox()

    with open(files, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(files, 'wb') as dec_file:
        dec_file.write(decrypted)

    print("DONE! ! !")
    time.sleep(3)
    os.system("cls")
    import keygen as key
    key.menu()
