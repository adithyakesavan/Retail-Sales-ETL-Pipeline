
import pandas as pd
import sqlite3
from pathlib import Path


def load_data():

    # Locate project directory
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Input and database paths
    INPUT_FILE = BASE_DIR / "output" / "clean_sales.csv"
    DB_FILE = BASE_DIR / "retail_sales.db"

    # Check input file
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Clean dataset not found: {INPUT_FILE}"
        )

    # Read cleaned data
    df = pd.read_csv(INPUT_FILE)

    print("LOADING STARTED")
    print(f"Records received: {len(df)}")

    # Connect to SQLite database
    with sqlite3.connect(DB_FILE) as conn:

        # Create table with explicit schema
        conn.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                order_id TEXT PRIMARY KEY,
                order_date TEXT NOT NULL,
                customer_id TEXT NOT NULL,
                product TEXT NOT NULL,
                category TEXT NOT NULL,
                quantity INTEGER NOT NULL CHECK(quantity > 0),
                unit_price REAL NOT NULL CHECK(unit_price > 0),
                region TEXT NOT NULL,
                revenue REAL NOT NULL CHECK(revenue >= 0)
            )
        """)

        # Make loading repeatable
        conn.execute("DELETE FROM sales")

        # Insert cleaned records
        df.to_sql(
            "sales",
            conn,
            if_exists="append",
            index=False
        )

        # Create indexes for faster queries
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_sales_date
            ON sales(order_date)
        """)

        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_sales_customer
            ON sales(customer_id)
        """)

        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_sales_category
            ON sales(category)
        """)

        # Verify database records
        count = conn.execute(
            "SELECT COUNT(*) FROM sales"
        ).fetchone()[0]

        total_revenue = conn.execute(
            "SELECT SUM(revenue) FROM sales"
        ).fetchone()[0]

    print("\nLOADING COMPLETED")
    print(f"Records loaded: {count}")
    print(f"Total revenue: {total_revenue:,.2f}")
    print(f"Database created: {DB_FILE}")


if __name__ == "__main__":
    load_data()
