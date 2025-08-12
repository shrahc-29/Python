print("Bank Application.\n")

#Python Program for a small basic Bank Application.

class Account:  # Class for a bank account
    def __init__(self, name, birthdate, age, address):  # Initializing and declaring variables
        self.name = name
        self.birthdate = birthdate
        self.age = age
        self.address = address
        self.balance = 0
        self.statements = []

    # FUNCTION FOR DEPOSIT
    def deposit(self, amount):  # Function for depositing amount
        if amount <= 0:
            print("Invalid! Enter valid amount.")
            return
        self.balance += amount
        self.statements.append(f"Deposit: Rs {amount}")
        print(f"Deposit of Rs {amount} successful.")

    # FUNCTION FOR WITHDRAWAL
    def withdraw(self, amount):  # Function for withdrawing amount
        if amount <= 0:
            print("Invalid! Enter valid amount.")
            return
        elif amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        self.statements.append(f"Withdrawal: Rs {amount}.")
        print(f"Withdrawal of Rs {amount} successful.")

    # FUNCTION FOR UPDATING
    def update_acc(self, new_address):  # Function for updating address
        self.address = new_address
        print("Address updated successfully.")

    # FUNCTION FOR DISPLAYING BALANCE
    def disp_balance(self):  # Function for displaying balance
        print(f"Current balance: Rs {self.balance}")

    # FUNCTION FOR PRINTING TRANSACTION HISTORY
    def disp_statement(self):  # Function for displaying transaction history
        print("\nTransaction Statement:")
        if not self.statements:
            print("No transactions found.")
        else:
            for statement in self.statements:
                print(statement)


class Bank:  # Class for accounts in a bank
    def __init__(self):
        self.accounts = {}

    def create_acc(self):
        acc_no = int(input("Enter Account Number: "))
        if acc_no in self.accounts:
            print("Account Number already exists.")
            return

        name = input("Enter Name: ")
        birthdate = input("Enter Birthdate: ")
        age = int(input("Enter Age in years: "))
        address = input("Enter Address: ")

        account = Account(name, birthdate, age, address)
        self.accounts[acc_no] = account
        print("Account created successfully.")

    def update_acc(self):
        acc_no = int(input("Enter account number to update: "))
        if acc_no not in self.accounts:
            print("Account not found.")
            return
        account = self.accounts[acc_no]
        new_address = input("Enter new address: ")
        account.update_acc(new_address)

    def dep_amt(self):
        acc_no = int(input("Enter account number to deposit: "))
        if acc_no not in self.accounts:
            print("Account not found.")
            return
        account = self.accounts[acc_no]
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    def wit_amt(self):
        acc_no = int(input("Enter account number to withdraw: "))
        if acc_no not in self.accounts:
            print("Account not found.")
            return
        account = self.accounts[acc_no]
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    def disp_bal(self):
        acc_no = int(input("Enter account number to display balance: "))
        if acc_no not in self.accounts:
            print("Account not found.")
            return
        account = self.accounts[acc_no]
        account.disp_balance()

    def disp_stmt(self):
        acc_no = int(input("Enter account number to display transaction history: "))
        if acc_no not in self.accounts:
            print("Account not found.")
            return
        account = self.accounts[acc_no]
        account.disp_statement()


def menu():
    bank = Bank()

    while True:
        print("\n\n***** Banking Application Menu *****")
        print("1. Create Account")
        print("2. Update Account")
        print("3. Deposit Amount")
        print("4. Withdraw Amount")
        print("5. Display Balance")
        print("6. Display Transaction History")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        print("\n")

        if choice == '1':
            bank.create_acc()
        elif choice == '2':
            bank.update_acc()
        elif choice == '3':
            bank.dep_amt()
        elif choice == '4':
            bank.wit_amt()
        elif choice == '5':
            bank.disp_bal()
        elif choice == '6':
            bank.disp_stmt()
        elif choice == '7':
            print("Exiting application. Thank you!")
            print("*********")
            break
        else:
            print("Invalid choice. Please try again.")


menu()
