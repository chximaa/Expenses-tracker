import os
import pandas as pd
import matplotlib.pyplot as plt

# CSV file path
file_path = "C:/Users/pc/OneDrive/Documentos/s5/projects/python/expenses.csv"

# Initialize CSV if it doesn't exist
def initialize_csv():
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
        df.to_csv(file_path, index=False)

# Add a new expense
def addExpense():
    Date = input("Enter the date (YYYY-MM-DD):\n")
    Category = input("Enter the category (e.g. Food, Transport, etc.):\n")
    try:
        Amount = float(input("Enter the amount spent:\n"))
    except ValueError:
        print("Amount must be a number!\n")
        return
    Description = input("Enter a short description:\n")

    expense = pd.DataFrame({
        "Date": [Date],
        "Category": [Category],
        "Amount": [Amount],
        "Description": [Description]
    })

    expense.to_csv(file_path, mode='a', header=False, index=False)
    print("✅ Expense added successfully!\n")

# View all expenses
def readExpenses():
    df = pd.read_csv(file_path)
    if df.empty:
        print("No expenses found!\n")
    else:
        print("\nYour Expenses:\n")
        print(df.to_string(index=True))
        print()

# Show total money spent
def totalMoney():
    df = pd.read_csv(file_path)
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    total = df["Amount"].sum()
    if total == 0:
        print("You haven't spent any money!\n")
    else:
        print(f"Total money spent is {total}.\n")

# Delete an expense by row index
def deleteExpense():
    df = pd.read_csv(file_path)
    if df.empty:
        print("No expenses to delete.\n")
        return

    print("\nYour Expenses:\n")
    print(df.to_string(index=True))
    try:
        x = int(input("Enter the row number of the expense you want to delete:\n"))
        if x in df.index:
            df = df.drop(index=x)
            df.to_csv(file_path, index=False)
            print("Expense deleted successfully!\n")
        else:
            print("Invalid row number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

# Visualize expenses
def visualize():
    df = pd.read_csv(file_path)
    if df.empty:
        print("No data to visualize!\n")
        return

    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Pie chart: Spending by Category
    category_totals = df.groupby("Category")["Amount"].sum()
    plt.figure(figsize=(7,7))
    plt.pie(category_totals, labels=category_totals.index, autopct="%1.1f%%", startangle=140)
    plt.title("Spending by Category")
    plt.show()

    # Line chart: Spending over time
    daily_totals = df.groupby("Date")["Amount"].sum()
    plt.figure(figsize=(10,5))
    plt.plot(daily_totals.index, daily_totals.values, marker="o", linestyle="-", color="blue")
    plt.title("Spending Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount Spent")
    plt.grid(True)
    plt.show()

    # Bar chart: Spending by Category
    plt.figure(figsize=(8,5))
    plt.bar(category_totals.index, category_totals.values, color="orange")
    plt.title("Total Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")
    plt.show()


#Modify an expense
def modifyExpence():
    df = pd.read_csv(file_path)
    if df.empty:
        print("There is no expence to modify.\n")
        return
    else :
        print("Your expenses are : \n")
        print(df.to_string(index=True))
    try:
        y = int(input("Enter the row number of the expense you want to modify:\n"))
        if y not in df.index:
            print("Invalid row number!\n")
            return
    except ValueError:
        print("Please enter a valid number!\n")
        return

    current_row = df.loc[y]
    new_date = input(f"Enter new date (current: {current_row['Date']}): ") or current_row['Date']
    new_category = input(f"Enter new category (current: {current_row['Category']}): ") or current_row['Category']
    new_amount = input(f"Enter new amount (current: {current_row['Amount']}): ") or current_row['Amount']
    new_description = input(f"Enter new description (current: {current_row['Description']}): ") or current_row['Description']

    df.at[y, "Date"] = new_date
    df.at[y, "Category"] = new_category
    df.at[y, "Amount"] = float(new_amount)
    df.at[y, "Description"] = new_description

    df.to_csv(file_path, index=False)
    print(" Expense modified successfully!\n")




# Main menu
def main():
    initialize_csv()
    print("Welcome to your Expense Tracker!\n")
    
    while True:
        print("1. Add new expense")
        print("2. View all expenses")
        print("3. See total money spent")
        print("4. Modify an expense")
        print("5. Delete an expense")
        print("6. Visualize your data")
        print("7. Exit")
        
        choice = input("Please select your choice:\n")
        
        if choice == "1":
            addExpense()
        elif choice == "2":
            readExpenses()
        elif choice == "3":
            totalMoney()
        elif choice == "4":
            modifyExpence()
        elif choice == "5":
            deleteExpense()
        elif choice == "6":
            visualize()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.\n")

# Run the program
if __name__ == "__main__":
    main()
