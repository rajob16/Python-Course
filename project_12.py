#1. Income and Expense Tracking
#code for file instalation
import pandas as pd
import os

# Initialize files for persistent tracking
def initialize_files():
    for file_name in ["income.csv", "expenses.csv"]:
        if not os.path.exists(file_name):
            pd.DataFrame(columns=["Date", "Amount", "Category"]).to_csv(file_name, index=False)

initialize_files()

"""This code checks if income.csv and expenses.csv exist. If not, it creates empty CSV files with headers: Date, Amount, and Category.


"""

#Logging Income and Expenses
# Log income or expense
def log_transaction(transaction_type):
    file_name = "income.csv" if transaction_type == "income" else "expenses.csv"
    data = pd.read_csv(file_name)

    # Input details
    date = input("Enter the date (YYYY-MM-DD): ")
    amount = float(input(f"Enter the {transaction_type} amount: "))
    category = input(f"Enter the {transaction_type} category (e.g., Salary, Food, Transport, Utilities): ")

    # Append the new transaction
    new_entry = {"Date": date, "Amount": amount, "Category": category}
    data = data.append(new_entry, ignore_index=True)

    # Save back to the CSV file
    data.to_csv(file_name, index=False)
    print(f"{transaction_type.capitalize()} logged successfully!")
#Income Example: Log salary as income.
#Expense Example: Log food or transport as an expense.
#Viewing Stored Data
def view_transactions(transaction_type):
    file_name = "income.csv" if transaction_type == "income" else "expenses.csv"
    data = pd.read_csv(file_name)

    if data.empty:
        print(f"No {transaction_type} records found.")
    else:
        print(f"\n--- {transaction_type.capitalize()} Records ---")
        print(data)
#Provide a simple menu for users to log and view transactions.
def main_menu():
    while True:
        print("\n--- Personal Finance Analyzer ---")
        print("1. Log Income")
        print("2. Log Expense")
        print("3. View Income")
        print("4. View Expenses")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            log_transaction("income")
        elif choice == "2":
            log_transaction("expense")
        elif choice == "3":
            view_transactions("income")
        elif choice == "4":
            view_transactions("expense")
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Initialize files and start the menu
initialize_files()
main_menu()

#2. Financial Insights
# Generate financial summary
def financial_summary():
    income_data = pd.read_csv("income.csv")
    expense_data = pd.read_csv("expenses.csv")

    # Calculate totals
    total_income = income_data["Amount"].sum()
    total_expenses = expense_data["Amount"].sum()
    net_savings = total_income - total_expenses

    # Display summary
    print("\n--- Financial Summary ---")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Savings: ${net_savings:.2f}")

    # Category-wise expense breakdown
    print("\n--- Category-wise Expense Breakdown ---")
    if total_expenses > 0:
        category_breakdown = expense_data.groupby("Category")["Amount"].sum()
        for category, amount in category_breakdown.items():
            percentage = (amount / total_expenses) * 100
            print(f"{category}: {percentage:.2f}%")
    else:
        print("No expenses recorded.")

#budget planning
# Set and manage budgets
def manage_budgets():
    budgets = pd.read_csv("budgets.csv")

    while True:
        print("\n--- Budget Planning ---")
        print("1. Set Budget")
        print("2. View Budget Status")
        print("3. Exit Budget Planning")
        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Enter the category to set a budget for: ")
            budget = float(input(f"Enter the budget for {category}: "))

            # Update or add budget
            if category in budgets["Category"].values:
                budgets.loc[budgets["Category"] == category, "Budget"] = budget
            else:
                budgets = budgets.append({"Category": category, "Budget": budget}, ignore_index=True)

            budgets.to_csv("budgets.csv", index=False)
            print(f"Budget for {category} updated successfully!")
        elif choice == "2":
            expenses = pd.read_csv("expenses.csv")
            print("\n--- Budget Status ---")
            for _, row in budgets.iterrows():
                category = row["Category"]
                budget = row["Budget"]
                spent = expenses[expenses["Category"] == category]["Amount"].sum()
                if spent > budget:
                    print(f"Over budget for {category}! Spent ${spent:.2f} (Budget: ${budget:.2f})")
                else:
                    print(f"{category}: Spent ${spent:.2f} (Budget: ${budget:.2f})")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
#Provide a menu for users to interact with the application.
def main_menu():
    while True:
        print("\n--- Personal Finance Analyzer ---")
        print("1. Log Income")
        print("2. Log Expense")
        print("3. View Financial Summary")
        print("4. Manage Budgets")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            log_transaction("income")
        elif choice == "2":
            log_transaction("expense")
        elif choice == "3":
            financial_summary()
        elif choice == "4":
            manage_budgets()
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Initialize files and start the menu
initialize_files()
main_menu()

#saving goals
# Function to view savings goals
def view_savings_goals():
    file_name = "savings_goals.csv"
    goals_data = pd.read_csv(file_name)

    if goals_data.empty:
        print("No savings goals found. Set one to get started!")
        return

    # Display goals and progress
    print("\n--- Savings Goals ---")
    for index, row in goals_data.iterrows():
        goal_amount = row["Goal Amount"]
        deadline = row["Deadline"]
        current_savings = row["Current Savings"]
        progress = (current_savings / goal_amount) * 100

        # Display goal details
        print(f"Goal {index + 1}:")
        print(f"  - Goal Amount: ${goal_amount:.2f}")
        print(f"  - Deadline: {deadline}")
        print(f"  - Current Savings: ${current_savings:.2f}")
        print(f"  - Progress: {progress:.2f}%")

        # Motivational messages
        if progress >= 100:
            print("  🎉 Congratulations! You have achieved this goal!")
        elif progress >= 75:
            print("  👍 Almost there! Keep up the great work!")
        elif progress >= 50:
            print("  🌟 You're halfway there! Keep saving!")
        else:
            print("  🚀 Start saving consistently to reach your goal.")
#update current savings
# Function to update current savings
def update_current_savings():
    file_name = "savings_goals.csv"
    goals_data = pd.read_csv(file_name)

    if goals_data.empty:
        print("No savings goals found. Set one to get started!")
        return

    # Display goals to update
    print("\n--- Update Current Savings ---")
    for index, row in goals_data.iterrows():
        print(f"{index + 1}. Goal: ${row['Goal Amount']} | Current Savings: ${row['Current Savings']} | Deadline: {row['Deadline']}")

    # Select a goal to update
    goal_index = int(input("Enter the goal number to update: ")) - 1
    if 0 <= goal_index < len(goals_data):
        new_savings = float(input("Enter the updated current savings amount: "))
        goals_data.at[goal_index, "Current Savings"] = new_savings

        # Save the updated data
        goals_data.to_csv(file_name, index=False)
        print("Current savings updated successfully!")
    else:
        print("Invalid goal number. Try again.")

#console based menu
def main_menu():
    while True:
        print("\n--- Personal Finance Analyzer ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Financial Summary")
        print("4. Manage Budgets")
        print("5. Set Savings Goal")
        print("6. Export Financial Report")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            log_transaction("income")
        elif choice == "2":
            log_transaction("expense")
        elif choice == "3":
            financial_summary()
        elif choice == "4":
            manage_budgets()
        elif choice == "5":
            set_savings_goal()
        elif choice == "6":
            export_report()
        elif choice == "7":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Initialize files and start the menu
initialize_files()
main_menu()
