import json
import os
from datetime import datetime

class Transaction:
    def __init__(self, amount, description, t_type, date=None):
        self.amount = amount
        self.description = description
        self.t_type = t_type
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "amount": self.amount,
            "description": self.description,
            "type": self.t_type,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):
        return Transaction(
            amount=data["amount"],
            description=data["description"],
            t_type=data["type"],
            date=data["date"]
        )

class BudgetTracker:
    def __init__(self, filename="budget_data.json"):
        self.transactions = []
        self.filename = filename
        self.load_data()

    def add_transaction(self, amount, description, t_type):
        t = Transaction(amount, description, t_type)
        self.transactions.append(t)

    def get_balance(self):
        income = sum(t.amount for t in self.transactions if t.t_type == "income")
        expenses = sum(t.amount for t in self.transactions if t.t_type == "expense")
        return income - expenses

    def show_transactions(self, filter_type=None):
        filtered = self.transactions
        if filter_type:
            filtered = [t for t in self.transactions if t.t_type == filter_type]
        for t in filtered:
            print(f"{t.date} - {t.t_type.upper()} - ${t.amount:.2f} - {t.description}")

    def save_data(self):
        data = [t.to_dict() for t in self.transactions]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r") as f:
            data = json.load(f)
            self.transactions = [Transaction.from_dict(d) for d in data]

    def run(self):
        while True:
            print("\n--- Budget Tracker ---")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Balance")
            print("4. View All Transactions")
            print("5. View Only Income")
            print("6. View Only Expenses")
            print("7. Save and Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                amount = float(input("Enter income amount: "))
                description = input("Enter description: ")
                self.add_transaction(amount, description, "income")
            elif choice == "2":
                amount = float(input("Enter expense amount: "))
                description = input("Enter description: ")
                self.add_transaction(amount, description, "expense")
            elif choice == "3":
                balance = self.get_balance()
                print(f"Current balance: ${balance:.2f}")
            elif choice == "4":
                self.show_transactions()
            elif choice == "5":
                self.show_transactions("income")
            elif choice == "6":
                self.show_transactions("expense")
            elif choice == "7":
                self.save_data()
                print("Data saved. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    tracker = BudgetTracker()
    tracker.run()
