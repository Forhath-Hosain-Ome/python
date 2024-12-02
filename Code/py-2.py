class BankAccount:
    def __init__(self, holder_name="Default User", initial_balance=0):
        self.holder_name = holder_name
        self.balance = initial_balance
        print(f"Account created for {self.holder_name} with an initial balance of {self.balance}.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited {amount}. Updated balance: {self.balance}.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew {amount}. Updated balance: {self.balance}.")

    def display_balance(self):
        print(f"Current balance: {self.balance}.")


# Main Function for User Interaction
def main():
    print("Welcome to the Bank Account Management System!")
    
    # User input for account setup
    holder_name = input("Enter the account holder's name: ")
    while True:
        try:
            initial_balance = float(input("Enter the initial balance: "))
            if initial_balance < 0:
                print("Initial balance cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    account = BankAccount(holder_name, initial_balance)

    # Transaction menu
    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            try:
                deposit_amount = float(input("Enter deposit amount: "))
                account.deposit(deposit_amount)
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        
        elif choice == '2':
            try:
                withdrawal_amount = float(input("Enter withdrawal amount: "))
                account.withdraw(withdrawal_amount)
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        
        elif choice == '3':
            account.display_balance()
        
        elif choice == '4':
            print("Thank you for using the Bank Account Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
