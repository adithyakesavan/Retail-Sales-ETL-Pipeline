
import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]


def test_clean_record_count():
    df = pd.read_csv(BASE_DIR / "output/clean_sales.csv")
    assert len(df) == 116


def test_rejected_record_count():
    df = pd.read_csv(BASE_DIR / "output/rejected_sales.csv")
    assert len(df) == 5


def test_no_duplicate_order_ids():
    df = pd.read_csv(BASE_DIR / "output/clean_sales.csv")
    assert df["order_id"].is_unique


def test_positive_quantities():
    df = pd.read_csv(BASE_DIR / "output/clean_sales.csv")
    assert (df["quantity"] > 0).all()


def test_revenue_calculation():
    df = pd.read_csv(BASE_DIR / "output/clean_sales.csv")
    expected = df["quantity"] * df["unit_price"]

    assert (df["revenue"] == expected).all()


def test_database_record_count():
    conn = sqlite3.connect(BASE_DIR / "retail_sales.db")

    count = conn.execute(
        "SELECT COUNT(*) FROM sales"
    ).fetchone()[0]

    conn.close()

    assert count == 116


def test_database_revenue():
    conn = sqlite3.connect(BASE_DIR / "retail_sales.db")

    revenue = conn.execute(
        "SELECT SUM(revenue) FROM sales"
    ).fetchone()[0]

    conn.close()

    assert revenue == 3888100
