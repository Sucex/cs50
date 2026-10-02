#1. create empty dictionary

expenses = {}

#2. add 3 expenses manually
expenses["food"] = 5000
expenses["transport"] = 3000
expenses["data"] = 2000

# new function - add expense
def add_expense(category, amount):a
    expenses[category] = amount
    print(f"Added {category}: N{amount}")

#3. print total
total = sum(expenses.values())
print(f"Total: N{total}")
print(f"Expenses: {expenses}")


