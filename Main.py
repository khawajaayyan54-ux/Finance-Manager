# import os
# import json
# import Add_budget

# def load_json(filename):
#     if os.path.exists(filename):
#         with open(filename, "r") as f:
#             return json.load(f)
#     return {}

# def show_summary():
#     amount = load_json("amount.json")
#     expense = load_json("expense.json")

#     total_amount = sum(amount.values())
#     total_expense = sum(expense.values())
#     summary = (total_amount)-(total_expense)

#     print("SUMMARY")
#     print(f"Total income : {total_amount}\nTotal Expense : {total_expense}\nIn Hand : {summary}")

# while True:
#     print("\n1. Add Expense")
#     print("2. Add Amount")
#     print("3. View Summary")
#     print("4. Exit")

#     choice = input("Choose: ")

#     if choice == "1":
#         Add_budget.add_expense()
#     elif choice == "2":
#         Add_budget.add_amount()
#     elif choice == "3":
#         show_summary()
#     elif choice == "4":
#         break
#     else:
#         print("Invalid choice")

import os
import json
import Add_budget

def load_json(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}

def show_summary():
    amount = load_json("amount.json")
    expense = load_json("expense.json")

    total_amount = sum(amount.values())
    total_expense = sum(expense.values())
    summary = total_amount - total_expense

    print("\nSUMMARY")
    print(f"Total income  : {total_amount:,}")
    print(f"Total expense : {total_expense:,}")
    print(f"In hand       : {summary:,}")

while True:
    print("\n1. Add Expense")
    print("2. Add Amount")
    print("3. View Summary")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        Add_budget.add_expense()
    elif choice == "2":
        Add_budget.add_amount()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
