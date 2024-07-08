import getpass

while True:
    user = input("Your username: ")
    password = getpass.getpass("Your password: ")
    try:
        user = str(user)
        if password != user:
            print("Successfully register.")
            break
        else:
            print("Username and password should not the same. Please, try again.")
    except:
        print("Invalid values. Please, try again.")


