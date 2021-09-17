import pyAesCrypt
import tkinter as tk
import easygui
import os
from os import stat, remove
from cryptography.fernet import Fernet
import tkinter.messagebox
from tkinter import *


password = ""

window = tk.Tk()
expvar = tkinter.IntVar()
exp = Checkbutton(text="Show file in explorer when done", variable=expvar)
exp.pack()


class MbConstants:
    MB_OKCANCEL = 1
    IDCANCEL = 2
    IDOK = 1


bufferSize = 128 * 1024


def pwd():
    global password
    try:
        password = open(easygui.fileopenbox(filetypes=["*.key"], default="*.key")).read()
    except TypeError:
        pass


def keygen():
    global password
    try:
        key = Fernet.generate_key()
        password = easygui.filesavebox(filetypes=["key.key"], default="key.key")
        with open(password, 'wb') as filekey:
            filekey.write(key)
        passwd = key
        password = passwd.decode("utf-8")
        password.replace(" ", password)
    except TypeError:
        pass


def encrypt():
    try:
        file = easygui.fileopenbox()
        with open(file, "rb") as fIn:
            with open(str(file) + ".enc", "wb") as fOut:
                pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
                tkinter.messagebox.showinfo("Encryption", "Done!")

        remove(file)
        if expvar.get() == 1:
            os.system("explorer /select," + str(file) + ".enc")
        else:
            pass

    except TypeError:
        pass


def decrypt():
    try:
        file = easygui.fileopenbox(filetypes=["*.enc"], default="*.enc")
        encfilesize = stat(file).st_size
        name = os.path.splitext(file)[0]
        with open(file, "rb") as fIn:
            try:
                with open(str(name), "wb") as fOut:
                    pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encfilesize)
                    tkinter.messagebox.showinfo("Encryption", "Done!")
            except ValueError:
                remove(file)

        decrpath = str(file).replace(".enc", " ")
        remove(file)
        if expvar.get() == 1:
            os.system("explorer /select," + decrpath)
        else:
            pass

    except TypeError:
        pass


def keyprint():
    tkinter.messagebox.showinfo("Key", "Key: " + password)


window.title("Encrypt")
window.geometry("854x480")
newkey = tk.Button(text="Load a key", command=pwd)
newkey.pack()
keygen = tk.Button(text="Generate a new key", command=keygen)
keygen.pack()
enc = tk.Button(text="Encrypt", command=encrypt)
enc.pack()
decr = tk.Button(text="Decrypt", command=decrypt)
decr.pack()
printkey = tk.Button(text="Print the key", command=keyprint)
printkey.pack()
alert = tk.Text(window)
alert.insert(tk.INSERT, "NOTE: For large files it can take some minutes. When done, you will be warned.")
alert.pack()
window.mainloop()
