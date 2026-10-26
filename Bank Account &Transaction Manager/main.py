from modules import *
from storage import *
def main():
    accounts = load_accounts(STORAGE_FILE)

    while True:
        print("\n" + "=" * 40)
        print("       BANK CORE SYSTEM (CLI)")
        print("=" * 40)
        print("1. Open New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Account & Transactions")
        print("5. Apply Interest (Savings Account)")
        print("6. Merge Two Accounts (+)")
        print("7. Save and Exit")
        print("=" * 40)

        choice = input("Select an option (1-7): ").strip()

        # 1. Open New Account
        if choice == "1":
            name = input("Enter account owner name: ").strip()
            if not name:
                print("Error: Name cannot be blank.")
                continue
            if name in accounts:
                print("Error: An account with this name already exists.")
                continue

            acc_type = input("Account Type (1: Standard / 2: Savings): ").strip()
            try:
                initial_bal = float(input("Initial balance (default 0): ") or 0)
                if acc_type == "2":
                    rate = float(input("Interest rate (e.g. 0.05 for 5%): ") or 0.05)
                    accounts[name] = SavingsAccount(name, initial_bal, rate)
                else:
                    accounts[name] = Account(name, initial_bal)
                print(f"Account for '{name}' was created successfully.")
            except ValueError as err:
                print(f"Validation Error: {err}")

        # 2. Deposit
        elif choice == "2":
            name = input("Enter account owner name: ").strip()
            account = accounts.get(name)
            if not account:
                print("Account not found.")
                continue
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            except ValueError as err:
                print(f"Error: {err}")

        # 3. Withdraw
        elif choice == "3":
            name = input("Enter account owner name: ").strip()
            account = accounts.get(name)
            if not account:
                print("Account not found.")
                continue
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            except ValueError as err:
                print(f"Error: {err}")

        # 4. View Details & Statement
        elif choice == "4":
            name = input("Enter account owner name: ").strip()
            account = accounts.get(name)
            if not account:
                print("Account not found.")
                continue
            print("\n" + str(account))
            if account.transactions:
                print("Transaction History:")
                for idx, tx in enumerate(account.transactions, start=1):
                    print(f"  {idx}. {tx['type']}: ${tx['amount']:.2f}")
            else:
                print("No transactions recorded yet.")

        # 5. Apply Interest
        elif choice == "5":
            name = input("Enter account owner name: ").strip()
            account = accounts.get(name)
            if not account:
                print("Account not found.")
                continue
            if isinstance(account, SavingsAccount):
                account.apply_interest()
            else:
                print("Notice: Interest can only be applied to Savings accounts.")

        # 6. Merge Two Accounts
        elif choice == "6":
            name1 = input("First account owner: ").strip()
            name2 = input("Second account owner: ").strip()
            acc1 = accounts.get(name1)
            acc2 = accounts.get(name2)

            if not acc1 or not acc2:
                print("Error: One or both accounts do not exist.")
                continue
            if acc1 is acc2:
                print("Error: Cannot merge an account with itself.")
                continue

            merged = acc1 + acc2
            accounts[merged.owner] = merged
            print(f"Created merged account: {merged}")

        # 7. Save and Exit
        elif choice == "7":
            save_accounts(accounts, STORAGE_FILE)
            print("System closed safely. Goodbye!")
            break

        else:
            print("Invalid selection. Please choose a number from 1 to 7.")


if __name__ == "__main__":
    main()