
import pandas as pd
from pathlib import Path

from extract import extract_data


def transform_data(df):

    # Work on a copy of extracted data
    df = df.copy()

    print("\nTRANSFORMATION STARTED")

    # Track why records are rejected
    df["rejection_reason"] = ""

    def mark_rejected(mask, reason):
        df.loc[mask, "rejection_reason"] = (
            df.loc[mask, "rejection_reason"]
            .apply(
                lambda old: f"{old}; {reason}" if old else reason
            )
        )

    # 1. Identify duplicate orders
    duplicate_mask = df.duplicated(
        subset=["order_id"],
        keep="first"
    )
    mark_rejected(duplicate_mask, "Duplicate order ID")

    # 2. Convert dates into proper datetime format
    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

    invalid_date_mask = df["order_date"].isna()
    mark_rejected(invalid_date_mask, "Invalid order date")

    # 3. Convert numeric columns
    df["quantity"] = pd.to_numeric(
        df["quantity"],
        errors="coerce"
    )

    df["unit_price"] = pd.to_numeric(
        df["unit_price"],
        errors="coerce"
    )

    # 4. Identify missing numeric values
    mark_rejected(
        df["quantity"].isna(),
        "Missing or invalid quantity"
    )

    mark_rejected(
        df["unit_price"].isna(),
        "Missing or invalid unit price"
    )

    # 5. Identify invalid quantities and prices
    mark_rejected(
        df["quantity"] <= 0,
        "Non-positive quantity"
    )

    mark_rejected(
        df["unit_price"] <= 0,
        "Non-positive unit price"
    )

    # 6. Check other required columns
    other_columns = [
        "order_id",
        "customer_id",
        "product",
        "category",
        "region"
    ]

    missing_fields = df[other_columns].isna().any(axis=1)

    mark_rejected(
        missing_fields,
        "Missing required field"
    )

    # Separate accepted and rejected records
    rejected_df = df[df["rejection_reason"] != ""].copy()

    clean_df = df[df["rejection_reason"] == ""].copy()

    # 7. Convert valid data types
    clean_df["quantity"] = clean_df["quantity"].astype(int)
    clean_df["unit_price"] = clean_df["unit_price"].astype(int)

    # 8. Calculate revenue
    clean_df["revenue"] = (
        clean_df["quantity"] * clean_df["unit_price"]
    )

    # Format date for output
    clean_df["order_date"] = (
        clean_df["order_date"].dt.strftime("%Y-%m-%d")
    )

    # Remove internal tracking column from clean data
    clean_df = clean_df.drop(columns=["rejection_reason"])

    print("\nTRANSFORMATION COMPLETED")
    print(f"Original records: {len(df)}")
    print(f"Clean records: {len(clean_df)}")
    print(f"Rejected records: {len(rejected_df)}")

    print("\nRejection breakdown:")
    print(rejected_df["rejection_reason"].value_counts().to_string())

    return clean_df, rejected_df


def save_transformed_data(clean_df, rejected_df):

    BASE_DIR = Path(__file__).resolve().parent.parent

    OUTPUT_DIR = BASE_DIR / "output"
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Save clean records
    clean_file = OUTPUT_DIR / "clean_sales.csv"
    clean_df.to_csv(clean_file, index=False)

    # Save rejected records for auditing
    rejected_file = OUTPUT_DIR / "rejected_sales.csv"
    rejected_df.to_csv(rejected_file, index=False)

    print("\nOUTPUT FILES CREATED")
    print(f"Clean data: {clean_file}")
    print(f"Rejected data: {rejected_file}")


if __name__ == "__main__":

    raw_df = extract_data()

    clean_df, rejected_df = transform_data(raw_df)

    save_transformed_data(clean_df, rejected_df)
