# Project Chart

## Veterinary Radiology Intelligence

This document provides the structure and workflow of the project.

---

## 1. Project Goal

The project analyzes veterinary radiology records to identify clinical, operational and referral patterns and transform those findings into useful analytical outputs and an interactive dashboard.

---

## 2. Project Structure

```text
Veterinary-Radiology-Intelligence/
│
├── .gitignore
├── README.md
├── PROJECT_CHART.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   │   └── CUADERNO RX.xlsx
│   │
│   └── processed/
│       └── radiology_clean.csv
│
├── notebooks/
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   └── 03_Exploratory_Data_Analysis.ipynb
│
├── reports/
│   ├── DATA_CLEANING_PLAN.md
│   └── EDA_INSIGHTS.md
│
├── docs/
│   ├── DATA_DICTIONARY.md
│   └── METHODOLOGY.md
│
├── sql/
│   ├── 01_data_exploration.sql
│   ├── 02_radiology_analysis.sql
│   └── README.md
│
├── app/
│   ├── app.py
│   └── assets/
│
├── images/
│   ├── eda/
│   └── dashboard/
│
└── tests/
    ├── test_data.py
    └── test_app.py