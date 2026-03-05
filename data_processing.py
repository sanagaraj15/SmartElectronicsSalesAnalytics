import numpy as np
def clean_data(df):
    df = df.fillna(0)
    df = df.drop_duplicates()
    return df
def manipulate_data(df):
    df["ProfitMargin"] = df["Revenue"] - df["Cost"]
    data_array = df.select_dtypes(include=[np.number]).to_numpy()
    stats = {
        "Mean": np.mean(data_array),
        "Max": np.max(data_array),
        "Min": np.min(data_array),
        "StdDev": np.std(data_array)
    }
    return df, stats