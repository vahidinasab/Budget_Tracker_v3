import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Household Monthly Budget Tracker")

# Emojis for each category
category_emojis = {
    "Essential Living Costs": "🏠",
    "Transport & Vehicle Costs": "🚗",
    "Lifestyle & Personal Expenses": "👗",
    "Leisure & Entertainment": "🎉",
    "Financial Commitments": "💳",
    "Emergency & Miscellaneous": "⚠️"
}

# User input for net income
income = st.text_input("Enter your Monthly Net Income (£)", "")

# Define expense categories
expense_categories = {
    "Essential Living Costs": [
        "Groceries & Household Items",
        "Mortgage/Rent",
        "Council Tax",
        "Gas & Electricity",
        "Water Bill",
        "Internet & Phone"
    ],
    "Transport & Vehicle Costs": [
        "Car Loan/Lease Payments",
        "Fuel (Petrol/Diesel/EV Charging)",
        "Public Transport & Taxi",
        "Car Insurance & Maintenance"
    ],
    "Lifestyle & Personal Expenses": [
        "Clothing & Accessories",
        "Beauty & Healthcare",
        "Dining Out & Coffee",
        "Subscriptions & Memberships"
    ],
    "Leisure & Entertainment": [
        "Travel & Holidays",
        "Events & Hobbies",
        "Retreat & Well-being"
    ],
    "Financial Commitments": [
        "Credit Card / Loan Repayments",
        "Other Bills & Subscriptions"
    ],
    "Emergency & Miscellaneous": [
        "Unexpected/Unplanned Expenses"
    ]
}

# Dictionary to store user inputs
expenses = {}

# Get user input for each expense category
st.subheader("Enter Your Expenses (£)")
for category, items in expense_categories.items():
    st.markdown(f"### {category_emojis.get(category, '')} {category}")
    for item in items:
        expenses[item] = st.text_input(f"{item}:", "")

# Calculate total expenses and remaining balance
try:
    total_expenses = sum(float(exp) for exp in expenses.values() if exp.strip())
    remaining_balance = float(income) - total_expenses if income.strip() else 0
except ValueError:
    st.warning("Please enter valid numerical values for all fields.")
    total_expenses = 0
    remaining_balance = 0

# Display results
st.subheader("Budget Summary")
st.write(f"### Total Expenses: £{total_expenses:,.2f}")
st.write(f"### Remaining Savings: £{remaining_balance:,.2f}")

# Bar chart visualization
if total_expenses > 0:
    st.subheader("Expense Breakdown")
    expense_data = {k: float(v) for k, v in expenses.items() if v.strip()}

    # Sort expense data by value for better visualization
    sorted_expenses = dict(sorted(expense_data.items(), key=lambda item: item[1], reverse=True))
    
    # Calculate the percentage of each expense
    total_cost = total_expenses + float(income) if income.strip() else total_expenses
    expense_percentages = {key: (value / total_cost) * 100 for key, value in sorted_expenses.items()}

    # Create bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(list(sorted_expenses.keys()), list(sorted_expenses.values()), color='skyblue')

    # Add labels with percentage and sum of costs
    for i, (category, value) in enumerate(sorted_expenses.items()):
        percentage = expense_percentages[category]
        ax.text(value, i, f"£{value:,.2f} ({percentage:.1f}%)", va='center', ha='left', color='black')

    ax.set_xlabel('Amount (£)')
    ax.set_title('Monthly Expense Breakdown')
    
    # Display Total Income and Total Expenses
    ax.barh("Total Income", float(income) if income.strip() else 0, color='green', alpha=0.5)
    ax.barh("Total Expenses", total_expenses, color='red', alpha=0.5)
    
    # Add text for Total Income and Total Expenses
    ax.text(float(income) if income.strip() else 0, len(sorted_expenses), f"Income: £{income}", ha='left', color='black')
    ax.text(total_expenses, len(sorted_expenses), f"Expenses: £{total_expenses:,.2f}", ha='left', color='black')
    
    st.pyplot(fig)

