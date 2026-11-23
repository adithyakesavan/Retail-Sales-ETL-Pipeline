# Retail Sales Data Engineering Pipeline

A Python-based end-to-end ETL pipeline that extracts retail sales data, performs data cleaning and validation, loads the processed data into SQLite, and generates SQL-based business analytics reports.

## Project Overview

This project demonstrates a complete data engineering workflow using Python, Pandas, SQLite, and SQL.

The pipeline processes raw retail sales records, identifies invalid and duplicate data, calculates revenue, stores validated records in a relational database, and generates business reports automatically.

## Architecture

```text
          RAW SALES DATA
                 |
                 v
          DATA EXTRACTION
                 |
                 v
        DATA TRANSFORMATION
          (Python + Pandas)
                 |
          +------+------+
          |             |
          v             v
    CLEAN DATA     REJECTED DATA
          |
          v
       SQLITE DATABASE
          |
          v
       SQL ANALYTICS
          |
          v
      BUSINESS REPORTS
          |
          v
       CSV EXPORTS
```

## Technologies Used

- Python 3
- Pandas
- SQLite
- SQL
- VS Code
- Git and GitHub

## Project Structure

```text
Retail-Sales-ETL-Pipeline/
│
├── data/
│   └── raw_sales.csv
│
├── src/
│   ├── generate_data.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── run_analytics.py
│
├── sql/
│   └── analytics.sql
│
├── output/
│   ├── clean_sales.csv
│   ├── rejected_sales.csv
│   └── analytics/
│       ├── 01_category_revenue.csv
│       ├── 02_top_products.csv
│       ├── 03_monthly_revenue.csv
│       ├── 04_region_revenue.csv
│       └── 05_top_customers.csv
│
├── main.py
├── requirements.txt
├── README.md
└── retail_sales.db
```

## ETL Pipeline Workflow

### 1. Data Generation

A synthetic retail sales dataset is generated with transaction information such as:

- Order ID
- Order date
- Customer ID
- Product
- Category
- Quantity
- Unit price
- Region

The generated dataset contains 121 records, including intentionally introduced data-quality issues.

### 2. Data Extraction

Python reads the raw CSV dataset for processing.

### 3. Data Transformation

Pandas performs data cleaning and validation:

- Handles missing quantities.
- Validates unit prices.
- Validates order dates.
- Identifies duplicate order IDs.
- Rejects non-positive quantities.
- Calculates revenue using quantity multiplied by unit price.
- Separates invalid records into a rejection file with rejection reasons.

### 4. Database Loading

The validated dataset is loaded into SQLite.

Database table: `sales`

The loading process uses a full-refresh approach and creates indexes to support common analytical queries.

### 5. SQL Business Analytics

Five analytical queries are executed:

1. Revenue by product category.
2. Top five best-selling products.
3. Monthly revenue trends.
4. Revenue by region.
5. Top five customers by spending.

### 6. Report Generation

The analytical results are exported into five separate CSV reports.

## Project Results

| Metric | Result |
|---|---:|
| Raw records | 121 |
| Clean records | 116 |
| Rejected records | 5 |
| Database records | 116 |
| Total revenue | 3,888,100 |
| SQL analytical queries | 5 |
| CSV analytical reports | 5 |

## Business Insights

- Electronics generated the highest revenue: 2,795,000.
- South was the highest-revenue region: 1,696,200.
- Mobile was the best-selling product by quantity: 60 units.
- October recorded the highest monthly revenue: 610,100.

## Installation and Execution

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Retail-Sales-ETL-Pipeline
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

### Step 3: Activate the environment

Windows PowerShell:

```powershell
venv\Scripts\activate
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Generate the sample dataset

```bash
python src/generate_data.py
```

### Step 6: Execute the complete pipeline

```bash
python main.py
```

The pipeline performs extraction, transformation, database loading, SQL analytics, and report generation.

## Output Files

The pipeline generates:

- `clean_sales.csv` — validated sales records.
- `rejected_sales.csv` — invalid records with rejection reasons.
- `retail_sales.db` — SQLite database.
- Five analytical CSV reports inside `output/analytics/`.

## Skills Demonstrated

- ETL pipeline development
- Data extraction and transformation
- Data quality validation
- Python programming
- Pandas data processing
- Relational database integration
- SQL aggregations and analytical queries
- Automated pipeline orchestration
- CSV report generation
- Project documentation

## Future Enhancements

- Integrate PostgreSQL.
- Add automated pipeline scheduling.
- Implement logging and exception monitoring.
- Add unit testing using Pytest.
- Build an interactive dashboard using Power BI.
- Implement incremental data loading.

## Author

Data Engineering Project | Retail Sales ETL Pipeline

Built as a hands-on project to demonstrate practical data engineering skills.