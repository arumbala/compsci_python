from pathlib import Path

import pandas as pd

def process_file():
    pd.set_option('display.width', None)
    pd.set_option('display.max_columns', None)

    # 1. Load the surfers.csv file and print its contents
    data_path = Path(__file__).parent.parent / 'data' / 'surfers.csv'
    df = pd.read_csv(data_path)
    print("=== Original Data ===")
    print(df)
    print()

    # 2. Remove surfers without an age or surf_styles value
    df_cleaned = df.dropna(subset=['age', 'surf_styles'])
    print("=== After Removing Surfers Without Age or Surf Styles ===")
    print(df_cleaned)
    print()

    # 3. Create a new column num_styles that counts the number of styles
    df_cleaned = df_cleaned.copy()
    df_cleaned['num_styles'] = df_cleaned['surf_styles'].apply(lambda x: len(x.split(', ')))
    print("=== With num_styles Column ===")
    print(df_cleaned)


if __name__ == "__main__":
    process_file()