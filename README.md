SQL Data Analysis Project

Overview

This project performs data analysis using Python, Pandas, and SQLite. It loads financial, industry, payment, and subscription data from CSV files into an in-memory SQLite database, executes SQL queries, and presents insights on client distribution, renewal rates, and financial trends.

Data Sources

The project uses four CSV files:

finanical_information.csv - Contains economic indicators such as inflation and GDP growth rates.

industry_client_details.csv - Stores details about clients, including industry and company size.

payment_information.csv - Includes client payments and transaction details.

subscription_information.csv - Tracks subscription start dates, end dates, and renewal status.

Analysis Performed

The script executes the following SQL queries:

Client Count by Industry - Determines the number of unique clients in 'Finance Lending' and 'Blockchain' industries.

Industry with Highest Renewal Rate - Identifies the industry with the most renewed subscriptions.

Average Inflation Rate for Renewed Subscriptions - Calculates the average inflation rate when subscriptions were renewed.

Median Amount Paid Per Year - Computes the median payment amount from transaction records.

Dependencies

Python 3.x

Pandas

SQLite3

How to Run

Ensure all required CSV files are available in the specified directory.

Install dependencies using:

pip install pandas

Execute the script:

python sql_analysis.py

Output

The script prints:

Number of clients in 'Finance Lending' and 'Blockchain'

Industry with the highest renewal rate

Average inflation rate during renewals

Median yearly payment amount

Notes

The script runs in-memory, meaning data will be lost upon termination.

Ensure CSV files match expected schemas to avoid errors.
