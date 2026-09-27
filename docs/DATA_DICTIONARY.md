# Data Dictionary

## Overview

This document describes the variables used in the processed veterinary radiology dataset.

The dataset contains records of radiology examinations and patient characteristics collected from a veterinary radiology service.

---

## Patient Information

| Variable | Description | Type |
|---|---|---|
| `patient_name` | Name or identifier of the veterinary patient | String |
| `species` | Species of the patient, such as CANINO, FELINO or CONEJO | Categorical |
| `breed` | Recorded breed or breed category of the patient | Categorical |
| `birth_date` | Date of birth of the patient | Date |
| `weight_kg` | Patient weight converted to kilograms | Numeric |
| `sex` | Recorded sex category in the source data | Categorical |
| `sterilized` | Recorded sterilization status | Categorical |

---

## Examination Information

| Variable | Description | Type |
|---|---|---|
| `exam_date` | Date on which the radiology examination was performed | Date |
| `radiograph_count` | Number of radiographic images recorded for the examination | Numeric |
| `medical_report` | Indicates whether a medical report was recorded for the examination | Categorical |

---

## Referring Veterinarian Information

| Variable | Description | Type |
|---|---|---|
| `referring_veterinarian` | Original referring veterinarian entry from the source data | String |
| `referring_veterinarian_clean` | Standardized version used for analytical grouping | String |

The standardized veterinarian field was created to reduce clearly identifiable differences in formatting, prefixes and typographical errors.

Ambiguous names were not automatically merged when there was insufficient evidence to identify them as the same veterinarian.

---

## Derived Variables

| Variable | Description | Type |
|---|---|---|
| `patient_age_years` | Estimated patient age in years at the time of examination, calculated from `exam_date` and `birth_date` | Numeric |
| `exam_year` | Year extracted from `exam_date` | Integer |
| `exam_month` | Month extracted from `exam_date` | Integer |

---

## Missing Values

Missing values are retained as missing when the original information was unavailable.

Missing values were not artificially imputed for the descriptive analyses presented in the exploratory analysis notebook.

The main variables with missing information include:

- `weight_kg`
- `patient_age_years`
- `sterilized`
- `medical_report`
- `radiograph_count`
- `sex`
- `species`
- `breed`
- `exam_date`

---

## Analytical Notes

The meaning of categorical values follows the available information in the source dataset.

For variables such as `sex`, `sterilized` and `medical_report`, the analysis preserves the original recorded categories rather than inferring undocumented meanings.

The processed dataset is used as the analytical source for the subsequent notebooks and dashboard.