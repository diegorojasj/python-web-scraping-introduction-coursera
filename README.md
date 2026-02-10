# 🔄 Python Web Scraping Pipeline

A simple **Extract, Transform, Load (ETL)** pipeline built with Python and pandas. This project downloads car dealership data from multiple file formats (CSV, JSON, XML), transforms it, and outputs a clean consolidated CSV file.

## 📋 Overview

The pipeline performs the following steps:

1. **Extract** — From Website table data.
2. **Transform** — From Website table data, transform the data, and selects the relevant columns: `car_model`, `price`, and `fuel`.
3. **Load** — Saves the transformed data as a single CSV file in the `output/` directory.

All operations are logged with timestamps to `etl.log`.

## 🏗️ Project Structure

```
├── main.py       # Main pipeline orchestrator
├── extraction.py     # Extract functions for CSV, JSON, and XML
├── transform.py      # Data transformation logic
├── load.py           # Load data to CSV
├── utils.py          # Utility functions (download, unzip, logging)
├── requirements.txt  # Python dependencies
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+

### Installation

```bash
# Clone the repository
git clone https://github.com/diegorojasj/python-web-scraping-introduction-coursera.git
cd python-web-scraping-introduction-coursera

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Pipeline

```bash
python -m main
```

The output file will be saved to `output/transformed_data.csv`.

## 📦 Dependencies

| Package  | Version |
|----------|---------|
| pandas   | 3.0.0   |
| requests   | 2.32.5   |
| beautifulsoup4     | 4.14.3   |
| bs4     | 0.0.2   |

## 📄 Data Source
This data source belong to Python Project for Data Engineering module 1 course in Coursera:
[IBM Developer Skills Network — Web Scraping Lab Dataset](https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films)