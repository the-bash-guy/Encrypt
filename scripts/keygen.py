import time

def keygen():
    from cryptography.fernet import Fernet

    key = Fernet.generate_key()

    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

    print("FILE GENERATED! ! !")
    time.sleep(3)
    menu()

def menu():
    import sys
    text = """Select:
        [1] Generate Key (First time only)
        [2] Encrypt
        [3] Decrypt
        [4] Exit\n"""
    action = input(text)
    if action == str(1):
        keygen()
    elif action == str(2):
        import encryptor as encr
        encr.encrypt()
    elif action == str(3):
        import decryptor as decr
        decr.decrypt()
    elif action == str(4):
        print("Closing. . .")
        time.sleep(3)
        sys.exit(0)
    else:
        print("Type the number correctly!")
        menu()


menu()
