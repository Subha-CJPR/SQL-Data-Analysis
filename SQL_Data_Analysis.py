# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Mi8pcOdCswIUCH2qUBJ1hvynjodCKjP-
"""

import pandas as pd
import sqlite3
import os

# File paths
data_files = {
    "financial_information": "/content/finanical_information.csv",
    "industry_client_details": "/content/industry_client_details.csv",
    "payment_information": "/content/payment_information.csv",
    "subscription_information": "/content/subscription_information.csv"
}

# Connect to SQLite database (in-memory for this script)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Load CSV files into SQL tables with error handling
for table_name, file_path in data_files.items():
    if os.path.exists(file_path):
        try:
            df = pd.read_csv(file_path)
            df.to_sql(table_name, conn, if_exists='replace', index=False)
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
    else:
        print(f"File not found: {file_path}")

# Debug: Check table schemas
for table_name in data_files.keys():
    cursor.execute(f"PRAGMA table_info({table_name})")
    print(f"Schema for {table_name}:", cursor.fetchall())

# 1. Count of Finance Lending & Blockchain Clients
query_1 = """
    SELECT COUNT(DISTINCT client_id)
    FROM industry_client_details
    WHERE industry IN ('Finance Lending', 'Blockchain');
"""
finance_blockchain_clients = cursor.execute(query_1).fetchone()[0]

# 2. Industry with Highest Renewal Rate
query_2 = """
    SELECT icd.industry, COUNT(si.client_id) AS renewals
    FROM subscription_information si
    JOIN industry_client_details icd ON si.client_id = icd.client_id
    WHERE si.renewed = 1
    GROUP BY icd.industry
    ORDER BY renewals DESC
    LIMIT 1;
"""
highest_renewal_industry = cursor.execute(query_2).fetchone()

# 3. Average Inflation Rate when Subscriptions were Renewed
query_3 = """
    SELECT AVG(fi.inflation_rate)
    FROM financial_information fi
    JOIN subscription_information si ON fi.start_date = si.start_date
    WHERE si.renewed = 1;
"""
avg_inflation_rate = cursor.execute(query_3).fetchone()[0]

# 4. Median Amount Paid Per Year
query_4 = """
    SELECT amount_paid
    FROM payment_information
    ORDER BY amount_paid;
"""
payment_values = [row[0] for row in cursor.execute(query_4).fetchall()]
median_payment = payment_values[len(payment_values) // 2] if payment_values else None

# Print results
print(f"Finance Lending & Blockchain Clients: {finance_blockchain_clients}")
if highest_renewal_industry:
    print(f"Industry with Highest Renewal Rate: {highest_renewal_industry[0]} ({highest_renewal_industry[1]} renewals)")
else:
    print("Industry with Highest Renewal Rate: No data available")
print(f"Average Inflation Rate at Renewal: {avg_inflation_rate}")
print(f"Median Amount Paid Per Year: {median_payment}")

# Close connection
conn.close()