import pyAesCrypt
import easygui
import os
import sys
import ctypes
from time import sleep
from os import stat, remove
from cryptography.fernet import Fernet


alert = "NOTE: FOR LARGE FILES IT WOULD TAKE SOME MINUTES."


class MbConstants:
    MB_OKCANCEL = 1
    IDCANCEL = 2
    IDOK = 1


bufferSize = 128 * 1024


def launcher():
    os.system("cls")
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
        os.system("cls")
        launcher()


def pwd():
    global password
    try:
        password = open(easygui.fileopenbox(filetypes=["*.key"], default="*.key")).read()
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
    try:
        key = Fernet.generate_key()

        with open(easygui.filesavebox(), 'wb') as filekey:
            filekey.write(key)
        pwd()
    except TypeError:
        print("Save the key!")
        sleep(1)
        keygen()


def encrypt():
    try:
        file = easygui.fileopenbox()
        with open(file, "rb") as fIn:
            save = easygui.filesavebox()
            print(alert)
            if file != save:
                with open(save, "wb") as fOut:
                    pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
            else:
                print("The filename is identical at the source file. Give it another name.")
                encrypt()
    except TypeError:
        print("Select file!")
        sleep(1)
        encrypt()

    launcher()


def decrypt():
    try:
        file = easygui.fileopenbox()
        encfilesize = stat(file).st_size

        with open(file, "rb") as fIn:
            save = easygui.filesavebox()
            print(alert)
            if file != save:
                try:
                    with open(save, "wb") as fOut:
                        pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encfilesize)
                except ValueError:
                    remove(file)
            else:
                print("The filename is identical at the source file. Give it another name.")
                decrypt()

    except TypeError:
        print("Select file!")
        sleep(1)
        decrypt()

    launcher()


def mbox(message, title):
    return ctypes.windll.user32.MessageBoxW(0, message, title, MbConstants.MB_OKCANCEL)


def msgbox():
    rc = mbox("Please load the key If you don't have the key select 'No'.", "Alert")
    if rc == MbConstants.IDOK:
        pwd()
        launcher()
    elif rc == MbConstants.IDCANCEL:
        keygen()
        launcher()


msgbox()
