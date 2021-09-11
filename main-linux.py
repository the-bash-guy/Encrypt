import pyAesCrypt
from easygui import *
import os
import sys
from time import sleep
from os import stat, remove
from cryptography.fernet import Fernet


alert = "NOTE: FOR LARGE FILES IT WOULD TAKE SOME MINUTES."


bufferSize = 128 * 1024


def launcher():
    print("\033c", end="")
    sel = input("""Select:
        [1] Encrypt
        [2] Decrypt
        [3] Exit
        key: displays key for checking\n""")
    if sel == str(1):
        encrypt()
    elif sel == str(2):
        decrypt()
    elif sel == str(3):
        sys.exit(0)
    elif sel == "key":
        keyprint()
    else:
        print("Type the number correctly.")
        sleep(1)
        launcher()


def pwd():
    global password
    try:
        password = open(fileopenbox(filetypes=["*.key"], default="*.key")).read()
    except TypeError:
        print("Select a key!")
        sleep(1)
        pwd()


def keyprint():
    print(password)
    print("Returning to menu. . .")
    sleep(2)
    launcher()


def keygen():
    global password
    try:
        key = Fernet.generate_key()
        password = filesavebox(filetypes=["key.key"], default="key.key")
        with open(password, 'wb') as filekey:
            filekey.write(key)
        passwd = key
        password = passwd.decode("utf-8")
    except TypeError:
        print("Save the key!")
        sleep(1)
        keygen()


def encrypt():
    try:
        file = fileopenbox()
        dir = os.path.dirname(file)
        with open(file, "rb") as fIn:
            print(alert)
            with open(str(file) + ".enc", "wb") as fOut:
                pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)


        remove(file)
        print("File saved to: " + dir)

    except TypeError:
        print("Select file!")
        sleep(1)
        encrypt()

    launcher()


def decrypt():
    try:
        file = fileopenbox(filetypes=["*.enc"], default="*.enc")
        dir = os.path.dirname(file)
        encfilesize = stat(file).st_size
        name = os.path.splitext(file)[0]
        with open(file, "rb") as fIn:
            print(alert)
            try:
                with open(str(name), "wb") as fOut:
                    pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encfilesize)

            except ValueError:
                remove(file)

        remove(file)
        print("File saved to: " + dir)

    except TypeError:
        print("Select file!")
        sleep(1)
        decrypt()

    launcher()


def msgbox(msg="Please load an existing .key file. If you don't have any key select 'cancel'", title="Alert"):

    if ccbox(msg, title):
        pwd()
        launcher()
    else:
        keygen()
        launcher()


msgbox()
