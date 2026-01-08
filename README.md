🚀 YC Market Intelligence Lake
An End-to-End Data Engineering Pipeline for Startup Market Research

This project is a production-grade data pipeline that automates the collection, transformation, and storage of YC startup data. It transitions a manual market research process into an optimized "Data Lake" architecture using the Modern Data Stack.
🛠️ The Tech Stack

    Ingestion: Selenium & WebDriver Manager (Dynamic Web Scraping).

    Processing: Python & Pandas (Data Normalization & Vectorized Logic).

    Storage: Apache Parquet (High-performance Columnar Storage).

    Querying: DuckDB (OLAP Database Engine).

    Environment: Virtual Environments (.venv) & requirements.txt.

🏗️ Architecture: The Medallion Approach

This project follows the Medallion Architecture to ensure data reliability and lineage:

    Bronze (Raw): Unstructured yc_20.json captured directly from the YC Directory.

    Silver (Cleaned): Standardized Parquet files where data is "flattened" and industry tags are normalized to uppercase for consistent analysis.

    Gold (Analytical): Query-ready tables in DuckDB for business intelligence.

🚀 How to Run

    Clone the Repository:
    Bash

git clone https://github.com/YourUsername/YC_scrapper.git
cd YC_scrapper

Setup Environment:
PowerShell

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt

    Run the Pipeline:

        python main.py (Ingestion)

        python data_cleaning.py (Transformation)

        python query_startups.py (Analysis)

📊 Key Engineering Features

    Dynamic Scraping: Handles Single Page Applications (SPAs) using Selenium's Explicit Waits.

    Schema Enforcement: Converts nested JSON lists into searchable, columnar Parquet formats.

    Data Quality Safeguards: Implements validation checks (null-value detection and row-count verification) to prevent "data poisoning".