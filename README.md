Electronics Sales Data Cleaning and Analysis

This project focuses on data preprocessing and analysis of an electronics product sales dataset using Python libraries such as NumPy and Pandas.

The dataset contains 78 columns of sales-related information, including product details, customer information, order data, delivery data, and inventory metrics.

📁 Project Structure
electronics_sales_project
│
├── electronics_sales_2025_random_dates.csv
├── data_loader.py
├── data_processing.py
└── sales_analysis.py
Files Explanation

electronics_sales_2025_random_dates.csv
Contains the electronics product sales dataset with 78 columns and 200 rows.

data_loader.py
Responsible for loading the CSV dataset using Pandas.

data_processing.py
Performs data cleaning and manipulation operations such as:

Filling missing values

Removing duplicate records

Creating new calculated columns

Preparing data for analysis

sales_analysis.py
Main program that runs the entire workflow and performs statistical analysis using NumPy.

⚙ Technologies Used

Python

NumPy

Pandas

CSV Data Processing

🔧 Data Cleaning Techniques

The project performs the following cleaning operations:

Handling missing values (fillna)

Removing duplicate rows (drop_duplicates)

Converting data types

Creating derived features such as ProfitMargin

📊 Data Manipulation and Analysis

The project performs statistical analysis using NumPy, including:

Mean calculation

Maximum value detection

Minimum value detection

Standard deviation computation

