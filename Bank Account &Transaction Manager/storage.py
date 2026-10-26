import json
import os 
from modules import Account , SavingsAccount
STORAGE_FILE = "bank_data.json"

def save_accounts(accounts: dict, filepath: str):
    """Serializes and saves all accounts into a JSON file."""
    dirname = os.path.dirname(filepath)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    serialized = {owner: acc.to_dict() for owner, acc in accounts.items()}
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(serialized, f, indent=4)
    print("All accounts have been saved successfully.")


def load_accounts(filepath: str) -> dict:
    """Reads JSON file and reconstructs Account instances."""
    if not os.path.exists(filepath):
        return {}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            accounts = {}
            for owner, details in data.items():
                if details.get("type") == "Savings":
                    acc = SavingsAccount(
                        owner=owner,
                        balance=details["balance"],
                        interest_rate=details.get("interest_rate", 0.05),
                    )
                else:
                    acc = Account(owner=owner, balance=details["balance"])
                acc.transactions = details.get("transactions", [])
                accounts[owner] = acc
            return accounts
    except Exception as error:
        print(f"Error loading records: {error}")
        return {}