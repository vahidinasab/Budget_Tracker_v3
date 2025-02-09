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
    "T

