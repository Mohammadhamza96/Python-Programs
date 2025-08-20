
from datetime import datetime

class BankAccount:
    
    
    def _init_(self, account_holder_name, initial_pin, starting_balance=0):
      
        self.account_holder_name = account_holder_name
        self._pin = initial_pin  
        self.balance = starting_balance
        self.transaction_history = []  
        self.daily_withdrawal_limit = 10000  

    def _verify_pin(self, entered_pin):
      
        return self._pin == entered_pin

    def deposit_funds(self, amount, entered_pin):
     
        if not self._verify_pin(entered_pin):
            print("Invalid PIN. Deposit operation failed.")
            return
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        self._record_transaction("Deposit", amount)
        print(f"Successfully deposited $ {amount}. New balance: $ {self.balance}")

    def withdraw_funds(self, amount, entered_pin):
     
        if not self._verify_pin(entered_pin):
            print("Invalid PIN. Withdrawal operation failed.")
            return
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.daily_withdrawal_limit:
            print(f"Withdrawal exceeds daily limit of ₹{self.daily_withdrawal_limit}.")
            return
        if amount > self.balance:
            print("Insufficient funds in the account.")
            return
        self.balance -= amount
        self._record_transaction("Withdrawal", amount)
        print(f"Successfully withdraw ₹{amount}. New balance: ₹{self.balance}")

    def _record_transaction(self, transaction_type, amount):
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append(f"{current_time} - {transaction_type}: ₹{amount}")

    def check_account_balance(self, entered_pin):
       
        if self._verify_pin(entered_pin):
            print(f"Current balance for {self.account_holder_name}: ₹{self.balance}")
        else:
            print("Invalid PIN. Cannot display balance.")

    def view_transaction_history(self, entered_pin):
       
        if self._verify_pin(entered_pin):
            print(f"Transaction History for {self.account_holder_name}:")
            if not self.transaction_history:
                print("No transactions recorded yet.")
            else:
                for record in self.transaction_history:
                    print(record)
        else:
            print("Invalid PIN. Cannot display history.")

    def update_pin(self, old_pin, new_pin):
       
        if not self._verify_pin(old_pin):
            print("Invalid old PIN. PIN change failed.")
            return
        if len(new_pin) != 4 or not new_pin.isdigit():
            print("New PIN must be exactly 4 digits.")
            return
        self._pin = new_pin
        print("PIN updated successfully.")

    def transfer_funds(self, amount, entered_pin, target_account):
      
        if not self._verify_pin(entered_pin):
            print("Invalid PIN. Transfer operation failed.")
            return
        if amount <= 0:
            print("Transfer amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Insufficient funds for transfer.")
            return
        self.balance -= amount
        target_account.balance += amount
        self._record_transaction("Transfer Out", amount)
        target_account._record_transaction("Transfer In", amount)
        print(f"Successfully transferred $ {amount} to {target_account.account_holder_name}.")
        print(f"Your new balance: $ {self.balance}")


def main():
 
    accounts = {}  

    while True:
        print("\n --- Banking Application Menu ---")
        print("1. Create New Account")
        print("2. Login to Existing Account")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            # Create a new account
            holder_name = input("Enter account holder name: ").strip()
            if holder_name in accounts:
                print("Account with this name already exists.")
                continue
            initial_pin = input("Set a 4-digit PIN: ").strip()
            if len(initial_pin) != 4 or not initial_pin.isdigit():
                print("PIN must be exactly 4 digits.")
                continue
            try:
                starting_balance = float(input("Enter initial deposit (optional, default 0): ").strip() or 0)
            except ValueError:
                print("Invalid amount. Using 0 as starting balance.")
                starting_balance = 0
            new_account = BankAccount(holder_name, initial_pin, starting_balance)
            accounts[holder_name] = new_account
            print(f"Account created successfully for {holder_name}.")

        elif choice == '2':
            # Login to an existing account
            holder_name = input("Enter account holder name: ").strip()
            if holder_name not in accounts:
                print("Account not found.")
                continue
            current_account = accounts[holder_name]
            entered_pin = input("Enter your PIN: ").strip()
            if not current_account._verify_pin(entered_pin):
                print("Invalid PIN. Login failed.")
                continue

            while True:
                print(f"\n --- Welcome, {holder_name} ---")
                print("1. Deposit Funds")
                print("2. Withdraw Funds")
                print("3. Check Balance")
                print("4. View Transaction History")
                print("5. Update PIN")
                print("6. Transfer Funds to Another Account")
                print("7. Logout")
                sub_choice = input("Enter your choice (1-7): ").strip()

                if sub_choice == '1':
                    try:
                        amount = float(input("Enter deposit amount: "))
                        current_account.deposit_funds(amount, entered_pin)
                    except ValueError:
                        print("Invalid amount.")

                elif sub_choice == '2':
                    try:
                        amount = float(input("Enter withdrawal amount: "))
                        current_account.withdraw_funds(amount, entered_pin)
                    except ValueError:
                        print("Invalid amount.")

                elif sub_choice == '3':
                    current_account.check_account_balance(entered_pin)

                elif sub_choice == '4':
                    current_account.view_transaction_history(entered_pin)

                elif sub_choice == '5':
                    old_pin = input("Enter old PIN: ").strip()
                    new_pin = input("Enter new 4-digit PIN: ").strip()
                    current_account.update_pin(old_pin, new_pin)

                elif sub_choice == '6':
                    target_name = input("Enter target account holder name: ").strip()
                    if target_name not in accounts or target_name == holder_name:
                        print("Invalid target account.")
                        continue
                    try:
                        amount = float(input("Enter transfer amount: "))
                        current_account.transfer_funds(amount, entered_pin, accounts[target_name])
                    except ValueError:
                        print("Invalid amount.")

                elif sub_choice == '7':
                    print("Logging out")
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == '3':
            print("Exiting the banking application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()