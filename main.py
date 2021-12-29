import subprocess
import sys
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
import easygui
import pyAesCrypt
import os
from os import stat, remove
from cryptography.fernet import Fernet
from pathlib import Path
import textwrap
kivy.require('2.0.0')
os.chdir(sys._MEIPASS)

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

password = ""

bufferSize = 128 * 1024


class Encrypt(BoxLayout):
    def __init__(self, **kwargs):
        super(Encrypt, self).__init__(**kwargs)

    @staticmethod
    def pwd():
        global password
        try:
            home = os.path.expanduser('~')
            password = open(easygui.fileopenbox(filetypes=["*.key"], default=home + "\\*.key")).read()
        except TypeError:
            pass

    @staticmethod
    def unload():
        global password
        password = ""

    @staticmethod
    def warn_nokey():
        popup = Popup(title='Error', content=Label(text='First, load a key'), size_hint=(None, None),
                      size=(300, 300))
        popup.open()

    @staticmethod
    def keygen():
        global password
        try:
            key = Fernet.generate_key()
            home = os.path.expanduser('~')
            password = easygui.filesavebox(filetypes=["key.key"], default=home + "\\key.key")
            with open(password, 'wb') as filekey:
                filekey.write(key)
            passwd = key
            decoded = passwd.decode("utf-8")
            password = decoded
        except TypeError:
            Encrypt.unload()

    def encrypt(self):
        global file
        if password == "" or None:
            self.warn_nokey()
        else:
            try:
                home = os.path.expanduser('~')
                file = easygui.fileopenbox(default=home + "\\*.*", multiple=True, title="Select files to encrypt")
                for i in file:
                    name = os.path.splitext(i)[0]
                    with open(i, "rb") as fIn:
                        try:
                            with open(name + ".tmp", "wb") as fOut:
                                subprocess.Popen([".\\Progress", i, name + ".tmp"])
                                pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
                        except ValueError:
                            remove(name + ".tmp")
                for i in file:
                    try:
                        name = os.path.splitext(i)[0]
                        if os.path.isfile(name + ".tmp"):
                            remove(i)
                        os.rename(name + ".tmp", i)
                    except FileNotFoundError:
                        pass
                message = 'Done: File(s) saved to:' + str(Path(file[0]).parent)
                popup = Popup(title='Success!', content=Label(text=textwrap.fill(message, 20)),
                              size_hint=(None, None),
                              size=(300, 300))
                popup.open()
            except TypeError:
                pass

    def decrypt(self):
        global file
        if password == "" or None:
            self.warn_nokey()
        else:
            try:
                home = os.path.expanduser('~')
                file = easygui.fileopenbox(default=home + "\\*.*", multiple=True, title="Select files to decrypt")
                for i in file:
                    name = os.path.splitext(i)[0]
                    encfilesize = stat(i).st_size
                    with open(i, "rb") as fIn:
                        try:
                            with open(name + ".tmp", "wb") as fOut:
                                subprocess.Popen([".\\Progress", i, name + ".tmp"])
                                pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encfilesize)
                        except ValueError:
                            remove(name + ".tmp")
                for i in file:
                    try:
                        name = os.path.splitext(i)[0]
                        if os.path.isfile(name + ".tmp"):
                            remove(i)
                        os.rename(name + ".tmp", i)
                    except FileNotFoundError:
                        pass
                message = 'Done: File(s) saved to:' + str(Path(file[0]).parent)
                popup = Popup(title='Success!', content=Label(text=textwrap.fill(message, 20)),
                              size_hint=(None, None),
                              size=(300, 300))
                popup.open()
            except TypeError:
                pass


class MainApp(App):
    title = "Encrypt V5.0"

    def build(self):
        return Encrypt()


app = MainApp()
app.run()
