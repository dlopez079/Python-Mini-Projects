master_pwd = input("What is the master password? ")

def view():
    print("You chose to view a password.")

def add():
    name = input("Enter Name: ")
    pwd = input("Enter Password: ")

    with open("passwords.text", "a") as f:
        f.write(name + "|" + pwd "\n")

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