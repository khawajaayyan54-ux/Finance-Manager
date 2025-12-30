import json
import os

def add_expense():
    filename = "expense.json"
    data = {}

    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)

    reason = input("Expense reason: ")
    while True:
        try:
            amount = int(input("Enter expense amount: "))
            if amount < 0:
                print("Amount cannot be negative")
                continue
            break
        except ValueError:
            print("Please enter numbers only")
    print("Your request has been granted and ur ammount has been transfered to expense")
    data[reason] = amount

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def add_amount():
    filename = "amount.json"
    data = {}

    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)

    reason = input("Income reason: ")
    while True:
        try:
            amount = int(input("Enter expense amount: "))
            if amount < 0:
                print("Amount cannot be negative")
                continue
            break
        except ValueError:
            print("Please enter numbers only")
    print("Your request has been granted and ur ammount has been transfered to amount")

    data[reason] = amount

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
