balance = 0
limit = 500
statement = ""
withdraw_count = 0
last_acc_number = 0
WITHDRAW_LIMIT = 3
ACC_AGENCY = "0001"

# Using dictionaries instead of lists
clients = {}
accounts = {}

def withdrawal(*, balance, amount, statement, limit, withdraw_count, withdraw_limit):
    exceeded_balance = amount > balance
    exceeded_limit = amount > limit
    exceeded_withdraws = withdraw_count >= withdraw_limit

    if exceeded_balance:
        print("Operation failed! You don't have enough balance.")
        return balance, statement, withdraw_count, False

    elif exceeded_limit:
        print("Operation failed! The withdrawal amount exceeds the limit.")
        return balance, statement, withdraw_count, False

    elif exceeded_withdraws:
        print("Operation failed! Maximum number of withdrawals exceeded.")
        return balance, statement, withdraw_count, False

    elif amount > 0:
        balance -= amount
        statement += f"Withdrawal: R$ {amount:.2f}\n"
        withdraw_count += 1
        retrieve_statement(balance, statement=statement)
        return balance, statement, withdraw_count, True
    else:
        print("Operation failed! The informed amount is invalid.")
        return balance, statement, withdraw_count, False


def deposit(balance, amount, statement, /):
    if amount > 0:
        balance += amount
        statement += f"Deposit: R$ {amount:.2f}\n"
        retrieve_statement(balance, statement=statement)
        return balance, statement
    else:
        print("Operation failed! The informed amount is invalid.")
        return False


def retrieve_statement(balance, /, *, statement):
    print("\n================ STATEMENT ================")
    print("No transactions have been made." if not statement else statement)
    print(f"\nBalance: R$ {balance:.2f}")
    print("===========================================")


def register_client(clients):
    cpf = input("What is your CPF? (only numbers) ").strip()
    full_name = input("What is your full name? ")
    address = input("What is your address? (street, number - neighborhood - city/state_abbreviation) ")
    
    if not cpf or not full_name.strip() or not address.strip():
        print("Operation failed! Missing information for registering new user.")
        return False

    if cpf in clients:
        print("Operation failed! CPF already registered.")
        return False

    clients[cpf] = {
        "full_name": full_name,
        "address": address
    }

    print(f"==== [i] {full_name} was registered in the system ====")
    return True


def create_checking_account(clients, accounts):
    owner_cpf = input("What is the CPF of the owner of this account? (only numbers) ")

    if owner_cpf not in clients:
        print("The informed CPF is not registered in the system.")
        return False

    global last_acc_number
    last_acc_number += 1
    accounts[last_acc_number] = {
        "agency": ACC_AGENCY,
        "owner_cpf": owner_cpf
    }

    owner_name = clients.get(owner_cpf)

    print(f"==== [i] Account {last_acc_number} with owner {owner_name} was registered in the system ====")
    return True


def handle_option(option):
    global balance, statement, withdraw_count
    
    if option == "u":
        register_client(clients=clients)

    elif option == "c":
        create_checking_account(clients=clients, accounts=accounts)

    elif option == "d":
        amount = float(input("Enter the deposit amount: "))
        balance, statement = deposit(balance, amount, statement)

    elif option == "s":
        amount = float(input("Enter the withdrawal amount: "))
        balance, statement, withdraw_count, success = withdrawal(balance=balance, amount=amount, statement=statement, limit=limit, withdraw_count=withdraw_count, withdraw_limit=WITHDRAW_LIMIT)
    
    elif option == "e":
        retrieve_statement(balance, statement=statement)

    elif option == "q":
        print("Exiting...")
        return False

    else:
        print("Invalid operation, please select again.")
    
    return True


def display_menu():
    menu = """

    [u] Create new user
    [c] Create new checking account
    [d] Deposit
    [s] Withdraw
    [e] Statement
    [q] Quit

    => """

    return input(menu)

def main():
    running = True
    while running:
        option = display_menu()
        running = handle_option(option)

if __name__ == "__main__":
    main()