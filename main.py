import subprocess
import pyAesCrypt
import tkinter as tk
import easygui
import os
from os import stat, remove
from cryptography.fernet import Fernet
import tkinter.messagebox
from tkinter import *
import sys

password = ""

window = tk.Tk()
expvar = tkinter.IntVar()
exp = Checkbutton(text="Show file in explorer when done", variable=expvar)
exp.pack()

bufferSize = 128 * 1024


def warn_nokey():
    easygui.msgbox("No key loaded. please load one.", ok_button="Load/Generate key")
    initkey = easygui.choicebox("Do you want to generate a new key or load an existing key?",
                                choices=['Load', 'Generate', 'Exit'])
    if initkey == "Load":
        pwd()
    elif initkey == "Generate":
        keygen()
    else:
        sys.exit(0)


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
    if password == "" or None:
        warn_nokey()
    else:
        try:
            file = easygui.fileopenbox()
            name = os.path.splitext(file)[0]
            with open(file, "rb") as fIn:
                with open(str(name) + ".tmp", "wb") as fOut:
                    proc1 = subprocess.Popen(["progress\\progress.exe"])
                    pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
            remove(file)
            os.rename(name + ".tmp", file)
            proc1.terminate()
            if expvar.get() == 1:
                os.system("explorer /select," + file)
            else:
                tkinter.messagebox.showinfo("Encryption", "Done! File saved to " + file)

        except TypeError:
            pass


def decrypt():
    if password == "" or None:
        warn_nokey()
    else:
        try:
            file = easygui.fileopenbox()
            encfilesize = stat(file).st_size
            name = os.path.splitext(file)[0]
            with open(file, "rb") as fIn:
                try:
                    with open(str(name) + ".tmp", "wb") as fOut:
                        proc1 = subprocess.Popen(["progress\\progress.exe"])
                        pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encfilesize)
                except ValueError:
                    remove(file)

            remove(file)
            os.rename(name + ".tmp", file)
            proc1.terminate()
            if expvar.get() == 1:
                os.system("explorer /select," + file)
            else:
                tkinter.messagebox.showinfo("Encryption", "Done! File saved to " + file)

        except TypeError:
            pass


def keyprint():
    try:
        tkinter.messagebox.showinfo("Key", "Key: " + password)
    except TypeError:
        warn_nokey()


window.title("Encrypt V4.2")
window.geometry("854x480")
newkey = tk.Button(text="Load a key", command=pwd)
newkey.pack()
keygener = tk.Button(text="Generate a new key", command=keygen)
keygener.pack()
enc = tk.Button(text="Encrypt", command=encrypt)
enc.pack()
decr = tk.Button(text="Decrypt", command=decrypt)
decr.pack()
printkey = tk.Button(text="Print the key", command=keyprint)
printkey.pack()
alert = tk.Text(window)
alert.insert(tk.INSERT, """NOTE: For large files it can take some minutes. When done, you will be warned.
WARNING: DO NOT INTERACT WITH THE WINDOW DURING ENCRYPTION/DECRYPTION PROCESS, AS THE WINDOW WILL NOT RESPOND.""")
alert.pack()
if password == "" or None:
    warn_nokey()
window.mainloop()
