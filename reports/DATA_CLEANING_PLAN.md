# Veterinary Radiology Data Cleaning Plan
## Project

Veterinary Radiology Intelligence

# Cleaning Workflow

The data cleaning process will be performed in a structured order.

Each step must be completed and validated before moving to the next one.

# Cleaning Tasks

| Step | Column | Problem | Cleaning Action | Status |
|------|---------|----------|-----------------|--------|
| 1 | Empty Columns | Completely empty columns | Remove unnecessary columns | ⬜ |
| 2 | Column Names | Inconsistent naming | Standardize column names | ⬜ |
| 3 | Species | Typographical errors | Standardize species names | ⬜ |
| 4 | Breed | Inconsistent writing | Standardize breed names | ⬜ |
| 5 | Birth Date | Mixed formats | Convert to datetime | ⬜ |
| 6 | Weight | Mixed values and NS | Convert to numeric and NaN | ⬜ |
| 7 | Sex | Inconsistent values | Standardize categories | ⬜ |
| 8 | Sterilization | Inconsistent values | Standardize categories | ⬜ |
| 9 | Referring Veterinarian | Different spellings | Standardize names | ⬜ |
| 10 | Radiograph Quantity | Mixed data types | Convert to numeric | ⬜ |
| 11 | Report | Unexpected values | Review and standardize | ⬜ |
| 12 | Contact | Mixed information | Standardize values | ⬜ |
| 13 | Final Validation | Verify dataset quality | Validate all transformations | ⬜ |

# General Cleaning Rules

1. Never modify data without evidence.

2. Preserve the original dataset.

3. Work on a copy of the dataset.

4. Document every transformation.

5. Validate each cleaning step before continuing.

6. Preserve clinically relevant information.

7. Missing values will never be replaced with invented information.

8. Every correction must be reproducible using Python code.

# Business Rules
The following business rules were defined based on veterinary domain knowledge.

## Species

- CANINO and FELINO are the main expected species.
- Misspellings will be corrected.
- Unknown values will be reviewed individually.

## Weight

- "NS" means the patient's weight was not recorded.
- Missing weight values will remain as missing.
- Decimal values will be standardized.

## Radiology Report

- "SI" indicates that a medical report was generated.
- "NO" indicates that no medical report was generated.
- Unexpected values will be investigated before modification.

## Referring Veterinarian

- Veterinarian names will be standardized.
- Titles such as DR., DRA., and VET. will be normalized.

## Contact

- Phone numbers will be preserved.
- SI and NO indicate whether contact with the owner was required.

# Data Quality Issues
The exploratory analysis identified the following issues:

- Missing values
- Empty columns
- Typographical errors
- Mixed date formats
- Inconsistent capitalization
- Mixed data types
- Duplicate categorical values
- Manual data entry inconsistencies
- Mixed information in some variables

# Validation Strategy
After each cleaning step, the following validations will be performed:

- Check missing values.
- Verify data types.
- Review unique values.
- Compare row counts.
- Ensure no information has been unintentionally removed.

# Expected Outcome
After completing the data cleaning process, the dataset should be:

- Consistent
- Standardized
- Reproducible
- SQL-ready
- Suitable for data visualization
- Ready for dashboard development
- Ready for machine learning applications
