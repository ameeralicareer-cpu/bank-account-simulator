import json
import os


# Step 1: Basic Account class
class Account:

    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    # Money account mein add karne ke liye
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return

        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    # Account se money nikalne ke liye
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be positive!")
            return

        if amount > self.balance:
            print("Insufficient balance!")
            return

        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    # Account ki information show karta hai
    def display(self):
        print(
            f"Account: {self.account_number} | "
            f"Holder: {self.holder_name} | "
            f"Balance: {self.balance}"
        )


# Step 2: Savings Account
class SavingsAccount(Account):

    def __init__(
        self,
        account_number,
        holder_name,
        balance=0,
        interest_rate=0.05
    ):
        # Parent class ki values set karna
        super().__init__(account_number, holder_name, balance)

        self.interest_rate = interest_rate

    # Savings account par interest add karta hai
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

        print(f"Interest added: {interest}")
        print(f"New balance: {self.balance}")


# Step 3: Current Account
class CurrentAccount(Account):

    def __init__(
        self,
        account_number,
        holder_name,
        balance=0,
        overdraft_limit=500
    ):
        super().__init__(account_number, holder_name, balance)

        self.overdraft_limit = overdraft_limit

    # Current account mein overdraft ki facility hoti hai
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be positive!")
            return

        if amount > self.balance + self.overdraft_limit:
            print("Overdraft limit exceeded!")
            return

        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")


# Step 4: Accounts ko JSON file mein save karna
def save_accounts(accounts, filename="accounts.json"):

    data = []

    for account in accounts:

        account_data = {
            "account_number": account.account_number,
            "holder_name": account.holder_name,
            "balance": account.balance
        }

        # Account ki type bhi save karni hai
        if isinstance(account, SavingsAccount):
            account_data["type"] = "SavingsAccount"
            account_data["interest_rate"] = account.interest_rate

        elif isinstance(account, CurrentAccount):
            account_data["type"] = "CurrentAccount"
            account_data["overdraft_limit"] = account.overdraft_limit

        else:
            account_data["type"] = "Account"

        data.append(account_data)

    # Data ko accounts.json file mein save karna
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

    print("Accounts saved!")


# Step 5: JSON file se accounts load karna
def load_accounts(filename="accounts.json"):

    # Agar file exist nahi karti to empty list return hogi
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as file:
        data = json.load(file)

    accounts = []

    # Saved data se dobara account objects banana
    for item in data:

        if item["type"] == "SavingsAccount":

            account = SavingsAccount(
                item["account_number"],
                item["holder_name"],
                item["balance"],
                item["interest_rate"]
            )

        elif item["type"] == "CurrentAccount":

            account = CurrentAccount(
                item["account_number"],
                item["holder_name"],
                item["balance"],
                item["overdraft_limit"]
            )

        else:

            account = Account(
                item["account_number"],
                item["holder_name"],
                item["balance"]
            )

        accounts.append(account)

    return accounts


# Step 6: Main menu
def main():

    # Program start hote hi saved accounts load karna
    accounts = load_accounts()

    # Menu baar baar show karne ke liye loop
    while True:

        print("\n================================")
        print("     BANK ACCOUNT SIMULATOR")
        print("================================")

        print("1. Create Savings Account")
        print("2. Create Current Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Display All Accounts")
        print("6. Save & Exit")

        choice = input("Enter choice: ")

        # Savings account create karna
        if choice == "1":

            account_number = input("Account number: ")
            holder_name = input("Holder name: ")
            balance = float(input("Initial balance: "))

            account = SavingsAccount(
                account_number,
                holder_name,
                balance
            )

            accounts.append(account)

            print("Savings Account created!")

        # Current account create karna
        elif choice == "2":

            account_number = input("Account number: ")
            holder_name = input("Holder name: ")
            balance = float(input("Initial balance: "))

            account = CurrentAccount(
                account_number,
                holder_name,
                balance
            )

            accounts.append(account)

            print("Current Account created!")

        # Account mein deposit karna
        elif choice == "3":

            account_number = input("Account number: ")
            amount = float(input("Deposit amount: "))

            # Account number se correct account find karna
            for account in accounts:

                if account.account_number == account_number:
                    account.deposit(amount)
                    break

            else:
                print("Account not found!")

        # Account se money withdraw karna
        elif choice == "4":

            account_number = input("Account number: ")
            amount = float(input("Withdraw amount: "))

            for account in accounts:

                if account.account_number == account_number:
                    account.withdraw(amount)
                    break

            else:
                print("Account not found!")

        # Saare accounts display karna
        elif choice == "5":

            if not accounts:
                print("No accounts found!")

            else:
                for account in accounts:
                    account.display()

        # Accounts save karke program close karna
        elif choice == "6":

            save_accounts(accounts)
            print("Goodbye!")
            break

        # Agar user 1-6 ke ilawa kuch enter kare
        else:
            print("Invalid choice, try again!")


# Program yahin se start hota hai
if __name__ == "__main__":
    main()