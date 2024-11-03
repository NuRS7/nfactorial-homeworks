users = {}
bank = {}  # Initialize the bank dictionary to store user balances
user_password = {}  # Initialize the user_password dictionary to store user passwords

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user_id = len(users)  # Generate a unique user ID
    users[user_id] = username
    user_password[user_id] = password
    bank[user_id] = 0  # Initialize the user's balance to 0

def add_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user_id = len(users)  # Generate a unique user ID
    users[user_id] = username
    user_password[user_id] = password
    bank[user_id] = 0  # Initialize the user's balance to 0
    print(f"User added with ID {user_id}")

def get_user(user_id):
    if user_id in users:
        return users[user_id]
    else:
        return "User not found"

def require_auth(func):
    def wrapper(user_id):
        password = input("Enter password: ")
        if user_id in user_password:
            if password == user_password[user_id]:
                print("Authorized")
                return func(user_id)
            else:
                print("Unauthorized")
        else:
            print("User not found")
    return wrapper

@require_auth
def get_balance(user_id):
    return bank[user_id]

def deposit(user_id):
    amount = float(input("Enter amount to deposit: "))
    if user_id in bank:
        bank[user_id] += amount
        print(f"Deposit successful. New balance for user ID {user_id}: {bank[user_id]}")
    else:
        print("User not found")

while True:
    command = input("Enter command:\n"
                    "1. Add user\n"
                    "2. Get user\n"
                    "3. Get balance\n"
                    "4. Deposit\n")

    if command == "1":
        add_user()
    elif command == "2":
        user_id = int(input("Enter user ID: "))
        print(get_user(user_id))
    elif command == "3":
        user_id = int(input("Enter user ID: "))
        print(get_balance(user_id))
    elif command == "4":
        user_id = int(input("Enter user ID: "))
        deposit(user_id)
    else:
        print("Invalid command. Please enter 1, 2, 3, or 4.")