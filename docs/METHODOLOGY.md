# Methodology

## 1. Project Overview

This project analyzes veterinary radiology records to identify clinical, operational and referral patterns within a veterinary radiology service.

The project follows a structured data workflow:

```text
Original Data
     ↓
Data Understanding
     ↓
Data Cleaning
     ↓
Clean Dataset
     ↓
Data Validation
     ↓
Exploratory Data Analysis
     ↓
Key Insights
     ↓
SQL Analysis
     ↓
Streamlit Dashboard

## 2. Data Understanding

The raw dataset (`CUADERNO RX.xlsx`) was first explored to identify column structure, data types, and initial quality issues, including inconsistent categories, missing values, and empty trailing columns.

## 3. Data Cleaning

The following cleaning steps were applied to produce the processed dataset:

- Column names were translated and standardized from Spanish to snake_case English identifiers.
- The `species` field was standardized to resolve inconsistent capitalization and formatting.
- Date fields (`exam_date`, `birth_date`) were converted to proper datetime types.
- The `referring_veterinarian` field was cleaned into `referring_veterinarian_clean` to reduce formatting differences, prefixes, and typographical errors. Ambiguous entries were left unmerged when there was insufficient evidence to treat them as the same person.
- Missing values were preserved rather than imputed, to maintain transparency about data completeness.

## 4. Derived Variables

Additional variables were calculated to support the analysis:

- `patient_age_years`, estimated from `birth_date` and `exam_date`.
- `exam_year` and `exam_month`, extracted from `exam_date`, to support temporal analysis.

## 5. Data Validation

After cleaning, the dataset was reviewed to confirm that categorical values, date ranges, and derived variables were consistent and did not introduce new errors during transformation.

## 6. Exploratory Data Analysis

The clean dataset was analyzed to identify patterns in species distribution, radiograph counts, medical report completion, and case volume over time. Findings and limitations are documented in `03_Exploratory_Data_Analysis.ipynb`.

## 7. SQL Analysis

The clean dataset was loaded into a PostgreSQL database (`public.radiology`). Parameterized SQL queries (see `sql/` and `queries.py`) were built to support year-range filtering and to calculate data quality metrics used in the dashboard.

## 8. Dashboard

Final results are presented through an interactive Streamlit dashboard, allowing users to filter results by year range and view key data quality indicators alongside the main visualizations.