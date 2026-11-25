# Retail Sales Data Engineering Pipeline

An end-to-end Retail Sales ETL Pipeline built using Python, Pandas, SQLite, SQL, Pytest, GitHub Actions, and Power BI.

This project demonstrates a complete data engineering workflow, from raw data extraction and transformation to database loading, business analytics, automated testing, and interactive dashboard development.

## Project Overview

The pipeline processes retail sales transactions, performs data cleaning and validation, stores clean records in an SQLite database, and generates SQL-based business analytics reports.

An interactive Power BI dashboard is built using the processed sales data to visualize revenue, products, customers, regional performance, and monthly sales trends.

## Project Architecture

```text
             RAW SALES DATA
                   |
                   v
            DATA EXTRACTION
                   |
                   v
          DATA TRANSFORMATION
             Python + Pandas
                   |
             +-----+-----+
             |           |
             v           v
         CLEAN DATA  REJECTED DATA
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
             |
             v
       POWER BI DASHBOARD
             |
             v
       BUSINESS INSIGHTS
```

## Technologies Used

- Python 3
- Pandas
- SQLite
- SQL
- Power BI Desktop
- DAX
- Pytest
- Git and GitHub
- GitHub Actions
- Visual Studio Code

## Project Structure

```text
Retail-Sales-ETL-Pipeline/
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── data/
│   └── raw_sales.csv
│
├── output/
│   ├── analytics/
│   │   ├── 01_category_revenue.csv
│   │   ├── 02_top_products.csv
│   │   ├── 03_monthly_revenue.csv
│   │   ├── 04_region_revenue.csv
│   │   └── 05_top_customers.csv
│   │
│   ├── clean_sales.csv
│   └── rejected_sales.csv
│
├── screenshots/
│   └── retail-sales-dashboard.png
│
├── sql/
│   └── analytics.sql
│
├── src/
│   ├── generate_data.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── run_analytics.py
│   └── logger_config.py
│
├── tests/
│   └── test_pipeline.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ETL Pipeline Workflow

### 1. Data Generation

A synthetic retail sales dataset is generated containing:

- Order ID
- Order date
- Customer ID
- Product
- Category
- Quantity
- Unit price
- Region

The original dataset contains 121 records, including intentionally introduced data-quality issues.

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

Validated records are loaded into an SQLite database.

Database table: `sales`

The loading process uses a full-refresh approach and creates indexes to support analytical queries.

### 5. SQL Business Analytics

Five analytical queries are executed:

1. Revenue by product category.
2. Top five best-selling products.
3. Monthly revenue trends.
4. Revenue by region.
5. Top five customers by spending.

The results are exported into five CSV analytical reports.

## Power BI Dashboard

An interactive Retail Sales Performance Dashboard was developed using Power BI Desktop.

The dashboard includes:

- Total Revenue KPI.
- Total Orders KPI.
- Total Customers KPI.
- Monthly Revenue Trend.
- Total Units Sold.
- Revenue by Region.
- Revenue by Category.
- Top 5 Products by Quantity Sold.
- Top 5 Customers by Revenue.

### Dashboard Preview

![Retail Sales Performance Dashboard](screenshots/retail-sales-dashboard.png)

## Project Results

| Metric | Result |
|---|---:|
| Raw records | 121 |
| Clean records | 116 |
| Rejected records | 5 |
| Database records | 116 |
| Total revenue | 3,888,100 |
| Total orders | 116 |
| Total customers | 39 |
| Total units sold | 357 |
| SQL analytical queries | 5 |
| CSV analytical reports | 5 |
| Automated tests | 7 |

## Business Insights

- Electronics generated the highest revenue: 2,795,000.
- South was the highest-revenue region: 1,696,200.
- Mobile was the best-selling product by quantity: 60 units.
- October recorded the highest monthly revenue: 610,100.
- CUST005 was the highest-spending customer: 417,800.

## Automated Testing

Pytest is used to validate the ETL pipeline.

The automated tests cover:

- Clean record count.
- Rejected record count.
- Duplicate order ID validation.
- Positive quantity validation.
- Revenue calculation.
- Database record count.
- Database revenue validation.

Test execution:

```bash
python -m pytest tests/ -v
```

**Test Results: 7 Passed**

## GitHub Actions – Continuous Integration

GitHub Actions automatically executes the pipeline and tests when changes are pushed to the repository.

The workflow includes:

1. Setting up Python.
2. Installing project dependencies.
3. Executing the ETL pipeline.
4. Running automated Pytest tests.

The CI workflow successfully completed with a passing build.

## Installation and Execution

### Step 1: Clone the repository

```bash
git clone https://github.com/adithyakesavan/Retail-Sales-ETL-Pipeline.git

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

Install Pytest if it is not included in the requirements:

```bash
python -m pip install pytest
```

### Step 5: Generate the sample dataset

```bash
python src/generate_data.py
```

### Step 6: Execute the complete ETL pipeline

```bash
python main.py
```

### Step 7: Run automated tests

```bash
python -m pytest tests/ -v
```

## Output Files

The pipeline generates:

- `clean_sales.csv` – validated sales records.
- `rejected_sales.csv` – invalid records with rejection reasons.
- `retail_sales.db` – SQLite database generated during execution.
- Five analytical CSV reports inside `output/analytics/`.

## Skills Demonstrated

- End-to-end ETL pipeline development.
- Data extraction and transformation.
- Data quality validation.
- Python programming.
- Pandas data processing.
- SQLite database integration.
- SQL aggregations and analytical queries.
- Automated pipeline orchestration.
- CSV report generation.
- Pytest automated testing.
- GitHub Actions continuous integration.
- Power BI dashboard development.
- Business intelligence and data visualization.
- Git version control.

## Future Enhancements

- Integrate PostgreSQL.
- Implement incremental data loading.
- Add automated pipeline scheduling.
- Integrate cloud storage.
- Implement advanced logging and exception monitoring.
- Develop additional business intelligence reports.

## GitHub Repository

[Retail Sales ETL Pipeline – GitHub](https://github.com/adithyakesavan/Retail-Sales-ETL-Pipeline)

## Author

**Adithya K**

Retail Sales Data Engineering Pipeline

Developed as a hands-on project to demonstrate practical Data Engineering, SQL, Python, automation, and Business Intelligence skills.