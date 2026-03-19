from resources import *
import getpass
while True:
    print("S-VAULT")
    action = authenticate()
    if action == 1:
        user_input = getpass.getpass("Enter Master Password: ")
        passer = login(user_input)
        if passer is None:
            pass
        elif passer:
            master_key = derive_key(user_input)
            print("\nWelcome")
            while True:
                action2 = after_login()
                if action2 == 1:
                    entered_app = input("New Password For- ")
                    entered_password = input("Enter The Password- ")
                    save_password(app=entered_app, password=entered_password, key= master_key)
                    print("Password Saved Successfully\n")
                elif action2 == 2:
                    while True:
                        limit = get_number("Generate With How Many Characters: ")
                        entered_password = generate_password(limit)
                        print(entered_password)
                        print("1. Save The Password")
                        print("2. Generate Another")
                        action3 = get_number("Action: ")
                        if action3 == 1:
                            entered_app = input("App Name: ")
                            save_password(app=entered_app, password=entered_password, key= master_key)
                            print("Password Saved Successfully\n")
                            break
                        elif action3 == 2:
                            continue
                        else:
                            print("Invalid Input")
                elif action2 == 3:
                    results = load_password()
                    if not results:
                        print("No passwords saved yet\n")
                    else:
                        print("\nPASSWORDS")
                        for cle,value in results.items():
                            print(f"{cle}- ********")
                        print("To Find Decrypted Passwords Use The Search Tool")
                        print("\n")
                elif action2 == 4:
                    results = load_password()
                    if not results:
                        print("No passwords saved yet\n")
                    else:
                        recherche = input("Search For Which App- ")
                        result = search_password(recherche, master_key)
                        if result:
                            print(f"Password for {recherche}: {result}\n")
                        else:
                            print("No Such App\n")
                else:
                    print("\n")
                    break
        else:
            print("Wrong Credentials\n")
    elif action == 2:
        user_input = getpass.getpass("Enter Master Password: ")
        create_account(user_input)
        print("Successfully Created\n")
    else:
        break