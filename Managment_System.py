# Bank Managment System

def show_menu():
    while True:
        print("\nMenu:")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Show Account Details")
        print("6. Show All Accounts")
        print("7. Exit")
        print()
        choice = int(input("Enter the Choice No (1-7): "))
        
        if choice == 1:
            add_account()
        elif choice == 2:
            check_balance()
        elif choice == 3:
            deposit()
        elif choice == 4:
            withdraw()
        elif choice == 5:
            show_account_details()
        elif choice == 6:
            show_all_accounts()
        elif choice == 7:
            break

customers = []

def add_account():
    name = input("Enter Account Holder Name: ")
    age = int(input("Enter Age: "))
    if age >= 18:
        password = input("Enter Password: ")
        initial_deposit = float(input("Enter the initial deposit: "))
        customers.append({
            "Name": name,
            "Age": age,
            "Pass": password,
            "Amt": initial_deposit
        })
        print(f"Account created successfully for {name}!")
        show_all_accounts()
    else:
        print("You are not eligible because you are underage.")

def show_all_accounts():
    print("\n-----------------All Accounts-----------------------")
    for index, acc in enumerate(customers, start=1):
        print(f"Acc ID: {index} - Account Holder: {acc['Name']}")
    print("----------------------------------------------------")

def get_account(acc_id):
    if 0 < acc_id <= len(customers):
        return customers[acc_id - 1]
    else:
        print("Invalid Account ID")
        return None

def check_balance():
    acc_id = int(input("Enter Account ID to check balance: "))
    acc = get_account(acc_id)
    if acc:
        print(f"""-----------------Account Summary-----------------------
Acc Id: {acc_id}
Account Holder Name: {acc['Name']}
Amount: {acc['Amt']} 
""")

def deposit():
    acc_id = int(input("Enter Account ID to deposit money: "))
    acc = get_account(acc_id)
    if acc and verify_password(acc):
        amount = float(input("Enter the amount to deposit: "))
        acc['Amt'] += amount
        print(f"Amount {amount} deposited successfully in account {acc_id}.")

def withdraw():
    acc_id = int(input("Enter Account ID to withdraw money: "))
    acc = get_account(acc_id)
    if acc and verify_password(acc):
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= acc['Amt']:
            acc['Amt'] -= amount
            print(f"Amount {amount} withdrawn successfully from account {acc_id}.")
        else:
            print("Insufficient balance.")

def show_account_details():
    acc_id = int(input("Enter Account ID to view details: "))
    acc = get_account(acc_id)
    if acc:
        print(f"""-----------------Account Holder Details-----------------------
Acc Id: {acc_id}
Account Holder Name: {acc['Name']}
Age: {acc['Age']}
Password: {acc['Pass']}
Amount: {acc['Amt']}
""")

def verify_password(account):
    password = input("Enter your password: ")
    if password == account['Pass']:
        return True
    else:
        print("Incorrect password.")
        return False

if __name__ == "__main__":
    show_menu()
