import pyAesCrypt
from easygui import *
import os
import sys
from time import sleep
from os import stat, remove
from cryptography.fernet import Fernet


bufferSize = 128 * 1024


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


alert = f"{bcolors.WARNING}NOTE: FOR LARGE FILES IT WOULD TAKE SOME MINUTES."


def launcher():
    print("\033c", end="")
    sel = input(f"""{bcolors.OKCYAN}Select:
        [1] Encrypt
        [2] Decrypt
        [3] Exit
        key: displays key for checking\n{bcolors.ENDC}""")
    if sel == str(1):
        encrypt()
    elif sel == str(2):
        decrypt()
    elif sel == str(3):
        sys.exit(0)
    elif sel == "key":
        keyprint()
    else:
        print(f"{bcolors.WARNING}Type the number correctly.{bcolors.ENDC}")
        sleep(1)
        launcher()


def pwd():
    global password
    try:
        password = open(fileopenbox(filetypes=["*.key"], default="*.key")).read()
    except TypeError:
        print(f"{bcolors.WARNING}Select a key!{bcolors.WARNING}")
        sleep(1)
        pwd()


def keyprint():
    print(password)
    print(f"{bcolors.OKBLUE}Returning to menu. . .{bcolors.ENDC}")
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
        print(f"{bcolors.WARNING}Save the key!{bcolors.ENDC}")
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
