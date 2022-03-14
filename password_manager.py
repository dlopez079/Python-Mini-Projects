from cryptography.fernet import Fernet

'''
This function should only be used once.  
After being used, comment it out.

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key



master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "/ Password: ", str(fer.encrypt(passw.encode())))

    print("You chose to view a password.")

def add():
    name = input("Enter Name: ")
    pwd = input("Enter Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")

    print("You successfully added the password.")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add, quit)? ")
    if mode == "quit":
        print("Quitter")
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else: 
        print("Invalide Mode. ")
        continue