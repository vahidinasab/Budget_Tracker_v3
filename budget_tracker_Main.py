import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Household Monthly Budget Tracker")

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
    st.markdown(f"### {category}")
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

# Pie chart visualization
if total_expenses > 0:
    st.subheader("Expense Breakdown")
    expense_data = {k: float(v) for k, v in expenses.items() if v.strip()}
    
    fig, ax = plt.subplots()
    ax.pie(expense_data.values(), labels=expense_data.keys(), autopct="%1.1f%%", startangle=90)
    ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle
    st.pyplot(fig)

