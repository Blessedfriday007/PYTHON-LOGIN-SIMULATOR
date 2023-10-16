import json
from colorama import Fore, Style
from getpass import getpass


# #############################################################
# UTILITIES
# #############################################################
def update_db(db: list) -> None:
    # This function is used to update the database list
    with open("db.txt", "w") as file:
        file.write(json.dumps(db))


def load_db() -> list:
    # This function is used to load database file
    with open("db.txt", "a+") as file:
        # return seek to index due to file append mode being used.
        file.seek(0)

        if data := file.read():
            return json.loads(data)
        return []


def check_user(db: list, username: str) -> bool:
    # This function is used to check if a user exisis in db list
    user = list(filter(lambda x: x.get("username") == username, db))
    return bool(user)


def get_user(db: list, username: str, password: str):
    # This function attempts to get user information from db list
    user = list(filter(lambda x: x.get("username") == username, db))

    if user and user[0].get("password") == password:
        return True, user[0]
    return False, None


# #############################################################
# PROCESSES
# #############################################################
def login():
    # get username and password
    username = input("Enter your username > ")
    password = getpass("Enter your password > ")

    db = load_db()
    return get_user(db, username, password)


def register():
    db = load_db()

    while True:
        # get username and password
        username = input("Enter your username > ")
        password = getpass("Enter your password > ")

        status = check_user(db, username)

        if status:
            print(f"{Fore.RED}User already exists... Try again!!{Style.RESET_ALL}")
            continue
        else:
            db.append({"username": username, "password": password})
            update_db(db)
            print(f"{Fore.GREEN}Registeration successful!!{Style.RESET_ALL}")
            break


def dashboard(user):
    db = load_db()

    while True:
        # Then welcome user and request for action
        msg = f"{Fore.GREEN}Welcome {user['username']}, please select an action:{Style.RESET_ALL} \n"
        msg += "(a) View our current user count \n"
        msg += "(b) delete account \n"
        msg += "(c) logout \n"
        print(msg)
        action = input("> ").lower()

        if action == "a":
            print(f"{Fore.BLUE}{len(db)} user records found!{Style.RESET_ALL}")
        elif action == "b":
            users = list(filter(lambda x: x.get("username") != user["username"], db))
            db = users
            update_db(db)
            msg = f"{Fore.GREEN}Account deleted successfully, user logged out, goodbye!!{Style.RESET_ALL}"
            print(msg)
            break
        elif action == "c":
            print(f"{Fore.GREEN}Logout successful!{Style.RESET_ALL}")
            break


def start():
    while True:
        # Then welcome user and request for action
        msg = """Welcome to pySimulator, please select an action: \n (a) Login \n (b) Register \n (c) Exit"""
        print(msg)
        action = input("> ").lower()

        if action == "a":
            status, user = login()
            if status:
                dashboard(user)
            else:
                print(f"{Fore.RED}Login failed, invalid credentials!{Style.RESET_ALL}")
        elif action == "b":
            register()
        elif action == "c":
            msg = f"{Fore.BLUE}Thank you for chooding pySimulator... Goodbye!{Style.RESET_ALL}"
            print(msg)
            raise SystemExit(0)
        else:
            msg = f'{Fore.RED}invalid action "{action}" selected, try again!{Style.RESET_ALL}'
            print(msg)


if __name__ == "__main__":
    start()
