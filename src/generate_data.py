
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

# Reproducible dataset
random.seed(42)

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = DATA_DIR / "raw_sales.csv"

# Dataset configuration
products = {
    "Laptop": ("Electronics", 55000),
    "Mobile": ("Electronics", 20000),
    "Headphones": ("Accessories", 2500),
    "Keyboard": ("Accessories", 1500),
    "Chair": ("Furniture", 7000),
    "Table": ("Furniture", 12000),
    "Shoes": ("Fashion", 3000),
    "TShirt": ("Fashion", 800),
    "Watch": ("Accessories", 5000),
    "Bag": ("Fashion", 1800)
}

regions = ["North", "South", "East", "West"]

columns = [
    "order_id",
    "order_date",
    "customer_id",
    "product",
    "category",
    "quantity",
    "unit_price",
    "region"
]

# Generate 120 valid sales records
records = []

start_date = datetime(2026, 1, 1)

for i in range(1, 121):

    product = random.choice(list(products.keys()))
    category, base_price = products[product]

    order_date = start_date + timedelta(
        days=random.randint(0, 300)
    )

    record = {
        "order_id": f"ORD{i:04d}",
        "order_date": order_date.strftime("%Y-%m-%d"),
        "customer_id": f"CUST{random.randint(1, 40):03d}",
        "product": product,
        "category": category,
        "quantity": random.randint(1, 5),
        "unit_price": base_price,
        "region": random.choice(regions)
    }

    records.append(record)

# Introduce intentional data-quality issues

# 1. Missing quantity
records[5]["quantity"] = ""

# 2. Missing unit price
records[12]["unit_price"] = ""

# 3. Invalid date
records[18]["order_date"] = "INVALID_DATE"

# 4. Negative quantity
records[25]["quantity"] = -3

# 5. Duplicate transaction
records.append(records[10].copy())

# Write dataset to CSV
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(file, fieldnames=columns)

    writer.writeheader()
    writer.writerows(records)

print("Dataset generated successfully!")
print(f"File location: {OUTPUT_FILE}")
print(f"Total records: {len(records)}")
