from data_loader import load_data
from data_processing import clean_data, manipulate_data
def main():
    df = load_data()
    print("\nCleaning Data...")
    df = clean_data(df)
    print("Manipulating Data...")
    df, stats = manipulate_data(df)
    print("\nDataset Preview")
    print(df.head())
    print("\nNumPy Statistics")
    for k,v in stats.items():
        print(k,":",round(v,2))
if __name__ == "__main__":
    main()