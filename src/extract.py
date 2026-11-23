
import pandas as pd
from pathlib import Path


def extract_data():

    # Locate project directory
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Raw data location
    INPUT_FILE = BASE_DIR / "data" / "raw_sales.csv"

    # Check whether file exists
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Raw dataset not found: {INPUT_FILE}"
        )

    # Read CSV using Pandas
    df = pd.read_csv(INPUT_FILE)

    print("EXTRACTION COMPLETED")
    print(f"Records extracted: {len(df)}")

    return df


if __name__ == "__main__":
    data = extract_data()
    print(data.head())
