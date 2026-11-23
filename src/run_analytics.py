
import sqlite3
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DB_FILE = BASE_DIR / "retail_sales.db"
SQL_FILE = BASE_DIR / "sql" / "analytics.sql"

REPORT_DIR = BASE_DIR / "output" / "analytics"


REPORT_NAMES = [
    "01_category_revenue.csv",
    "02_top_products.csv",
    "03_monthly_revenue.csv",
    "04_region_revenue.csv",
    "05_top_customers.csv"
]


def run_analytics():

    print("=" * 55)
    print("       RETAIL SALES BUSINESS ANALYTICS")
    print("=" * 55)

    # Create analytics output directory
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    # Read SQL queries
    sql_content = SQL_FILE.read_text(encoding="utf-8")

    queries = [
        query.strip()
        for query in sql_content.split(";")
        if "SELECT" in query.upper()
    ]

    if len(queries) != len(REPORT_NAMES):
        raise ValueError(
            f"Expected {len(REPORT_NAMES)} SQL queries, "
            f"found {len(queries)}"
        )

    with sqlite3.connect(DB_FILE) as conn:

        for index, query in enumerate(queries):

            report_name = REPORT_NAMES[index]

            print(f"\nQUERY {index + 1}")
            print("-" * 55)

            # Execute SQL query
            result = pd.read_sql_query(query, conn)

            # Display result
            print(result.to_string(index=False))

            # Export result to CSV
            report_path = REPORT_DIR / report_name

            result.to_csv(
                report_path,
                index=False
            )

            print(f"\nReport saved: {report_name}")

    print("\n" + "=" * 55)
    print("ALL ANALYTICS REPORTS EXPORTED SUCCESSFULLY")
    print("=" * 55)


if __name__ == "__main__":
    run_analytics()
