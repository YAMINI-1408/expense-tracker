# ADD EXPENSE
def add_expense(expenses, amount, category):
    expense = {
        "amount": amount,
        "category": category
    }
    expenses.append(expense)


#  TOTAL EXPENSE
def calculate_total_expense(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


# CATEGORY TOTAL 
def calculate_category_totals(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals
expenses = []

while True:
    print("\n1. Add Expense")
    print("2. Show Summary")
    print("3. Exit")

    choice = input("Enter choice: ")

    # ADD EXPENSE
    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food/Travel/etc): ")
        add_expense(expenses, amount, category)
        print("✅ Expense added!")

    # SHOW REPORT
    elif choice == "2":
        print("\nAll Expenses:", expenses)

        total = calculate_total_expense(expenses)
        print("Total Expense:", total)

        category_totals = calculate_category_totals(expenses)
        print("\nCategory-wise Expenses:")
        for category in category_totals:
            print(category, ":", category_totals[category])

    elif choice == "3":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice!")
