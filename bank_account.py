class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Enter a valid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful.")

    def check_balance(self):
        print("Current Balance:", self.balance)

    def display_details(self):
        print("\nAccount Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


name = input("Enter account holder name: ")
account_number = input("Enter account number: ")

account = BankAccount(name, account_number)

while True:
    print("\n--- Bank Account Management System ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Display Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        account.display_details()

    elif choice == "5":
        print("Thank you for using our banking application.")
        break

    else:
        print("Invalid choice. Please try again.")