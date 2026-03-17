from resources import *
while True:
    print("S-VAULT")
    action = authenticate()
    if action == 1:
        user_input = input("Enter Master Password: ")
        if login(user_input):
            print("proceed to next menu")
        else:
            print("wrong credentials")
    elif action == 2:
        user_input = input("Enter Master Password: ")
        create_account(user_input)
    else:
        break