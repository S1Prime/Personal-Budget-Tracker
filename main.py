#Personal Budget Tracker

expenseslst=[] #list of expenses in form of dictionaries
print("Welcome to Personal Budget Tracker")

while True:
    print("===Menu===")
    print("1.Add Expenses")
    print("2.View Expenses")
    print("3.View Total Expenses")
    print("4.Exit Menu")
#1.Adding Expenses
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
            "Amount": amt
        }
        expenseslst.append(expense)#for storing the data in expenses 
        print("\n Expenses Added Succesfully")

#2.Viewing Expenses
    elif (choice==2):
        if (len(expenseslst)==0):
            print("No expenses found")
        else:
            print("===This is the expenses===")
            count=1
            for exp in expenses:
                print(f"Expense No {count}=> {exp["Date"]},{exp["category"]},{exp["Description"]},{exp["Amount"]} ")
                count+=1 #Expense will be increased by 1

#3.Viewing Total Expenses
    elif (choice==3):
        total=0
        for krcha in expenseslst:
            total=total + krcha["Amount"]
        print("\n Total Expense is :",total)

#4.Exiting the Menu
    elif (choice==4):
        print("Thank You for using Personal Budget Tracker")
        break

    else:
        print("Invalid Choice.TRY AGAIN")



        

