Income and Expense Tracking:
import csv
import json
import datetime

def log_income():
  """Logs income with date and amount."""
  date = input("Enter date (YYYY-MM-DD): ")
  amount = float(input("Enter amount: "))
  source = input("Enter source (e.g., salary, freelancing): ")
  with open('income.csv', 'a', newline='') as file:  # Using CSV for simplicity
    writer = csv.writer(file)
    writer.writerow([date, amount, source])
  print("Income logged successfully!")

def log_expense():
  """Logs expense with date, amount, and category."""
  date = input("Enter date (YYYY-MM-DD): ")
  amount = float(input("Enter amount: "))
  category = input("Enter category (e.g., food, transport): ")
  with open('expenses.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([date, amount, category])
  print("Expense logged successfully!")

def calculate_summary():
  """Calculates total income, expenses, and net savings."""
  total_income = 0
  total_expenses = 0

  with open('income.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row if any
    for row in reader:
      total_income += float(row[1])  # Assuming amount is in the second column

  with open('expenses.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row if any
    for row in reader:
      total_expenses += float(row[1])

  net_savings = total_income - total_expenses
  print("Total Income:", total_income)
  print("Total Expenses:", total_expenses)
  print("Net Savings:", net_savings)

def set_budget():
  """Allows users to set monthly budget limits for categories."""
  # Implement budget setting logic here
  # This could involve creating a new CSV or JSON file to store budget limits
  # and then comparing actual expenses to these limits in other functions.
  pass  # Placeholder for budget setting

def check_budget():
  """Checks if expenses exceed budget limits and notifies the user."""
  # Implement budget checking logic here
  pass  # Placeholder for budget checking

def set_savings_goal():
  """Allows users to set savings goals and track progress."""
  # Implement savings goal setting and tracking logic here
  pass  # Placeholder for savings goal setting

def track_savings_progress():
  """Provides motivational messages based on savings progress."""
  # Implement savings progress tracking and motivation logic here
  pass  # Placeholder for progress tracking

import matplotlib.pyplot as plt

def visualize_expenses():
  """Visualizes expenses using pie charts or line charts."""
  # Implement visualization logic using matplotlib or ASCII art
  pass  # Placeholder for visualization

def main():
  """Provides a console-based menu for user interaction."""
  while True:
    print("\nPersonal Finance Analyzer")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Set Budget")
    print("5. Set Savings Goal")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      log_income()
    elif choice == '2':
      log_expense()
    elif choice == '3':
      calculate_summary()
    elif choice == '4':
      set_budget()  # Call the budget setting function (to be implemented)
    elif choice == '5':
      set_savings_goal()  # Call the savings goal function (to be implemented)
    elif choice == '6':
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
