#Personal Budget Tracker

expenses=[] #list of expenses in form of dictionaries
print("Welcome to Personal Budget Tracker")

while True:
    print("===Menu===")
    print("1.Add Expenses")
    print("2.Exit Menu")
    print("3.View Expenses")
    print("4.View Total Expenses")

    choice = input("Enter Your Choice:")
    if choice == "1":
        date = int(input("Enter the date:"))
        category = input("Enter the type of Expense(Food,Travel,Stationery): ")
        desc = input("Enter your description:")
        amt = int(input("Enter the amount:"))
        expense = {
            "Date": date,
            "category": category,
            "Description": desc,
            "Amount Spend": amt
        }
        expenses.append(expense)
    if (choice==2):
    if (choice==3):
    if (choice==4):

