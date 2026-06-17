# Data Governance & Migration Readiness Dashboard 📊

## Overview
Before enterprise systems can be modernized or migrated to the cloud (GCP, AWS, Azure), legacy data must be meticulously profiled for structural integrity and governance compliance. The **Data Governance & Migration Readiness Dashboard** is an automated, Streamlit-based profiling tool designed to accelerate the pre-migration discovery phase. 

It ingests raw, uncleaned legacy datasets and instantly generates an executive-level health score, visualizes data topography, and exports actionable remediation reports for primary key violations.

## 🚀 Key Features
* **Automated Data Discovery:** Instantly parses legacy CSV extracts to map out total records, attributes, and overall data health.
* **Completeness & Structural Integrity Profiling:** Visualizes missing data distribution (null values) across all columns and charts data type anomalies to ensure target schema compatibility.
* **Migration Readiness Scoring:** Calculates a weighted health score based on data completeness and uniqueness, mimicking enterprise consulting assessment frameworks.
* **Actionable Remediation Hub:** Detects primary key collision risks (duplicate records) and provides a direct download link for the dirty data, allowing data engineers to remediate issues prior to ETL pipelines.
* **Dark-Mode Enterprise UI:** Custom CSS-injected interface featuring tabbed navigation, gradient metric cards, and responsive Plotly visualizations.

## 🛠️ Tech Stack
* **Frontend/Framework:** Streamlit
* **Data Processing:** Pandas, NumPy
* **Data Visualization:** Plotly Express

## 📂 Project Structure
```text
migration-profiler-project/
├── app.py                      # Main Streamlit application
├── generate_dummy_data.py      # Script to generate a messy test dataset
├── legacy_financial_data.csv   # The sample legacy dataset
├── duplicate_records_report.csv# Auto-generated remediation export
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## 👨‍💻 Author
Aditya Aspiring Software Developer & Data Scientist with a focus on full-stack development, machine learning, and data transformation solutions.
