import pandas as pd
def load_data():
    df = pd.read_csv("electronics_sales_2025_random_dates.csv")
    print("Dataset Loaded Successfully")
    print("Shape:", df.shape)
    return df