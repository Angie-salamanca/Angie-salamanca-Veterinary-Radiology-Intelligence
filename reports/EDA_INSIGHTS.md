# EDA Insights

## Overview

The exploratory analysis of the veterinary radiology dataset identified several clinical, operational and referral patterns that can support future dashboard development and service monitoring.

---

## 1. Patient Population

Canine patients represented the majority of radiology records, with 496 cases (71.57%), followed by feline patients with 193 cases (27.85%).

Only one rabbit case was recorded, so this observation should not be generalized.

Species information was missing in 3 records.

---

## 2. Breed Distribution

The dataset contains a wide variety of recorded breeds.

CRIOLLO was the most frequently recorded breed, with 256 radiology cases, followed by FRENCH POODLE with 63 cases and MESTIZO with 41 cases.

Breed information was missing in 7 records.

---

## 3. Sex Distribution

The sex distribution was relatively balanced between canine and feline patients.

Among canine patients, 54.8% were recorded as H and 45.2% as M.

Among feline patients, 54.5% were recorded as H and 45.5% as M.

Ten records had missing sex information.

---

## 4. Sterilization

Sterilization information was available for 595 records.

Among records with available information, 61.0% were marked as sterilized and 39.0% as not sterilized.

Within species, feline patients showed a higher proportion of sterilized records (76.4%) compared with canine patients (55.2%).

---

## 5. Patient Age

Among the 531 records with available age information, the mean patient age was 6.77 years and the median was 6.54 years.

A total of 71 patients were younger than one year.

Age information was missing in 162 records.

Canine patients were generally older than feline patients in the available records, with mean ages of 7.57 and 4.72 years respectively.

---

## 6. Patient Weight

Weight information was available for 595 records.

The mean patient weight was 12.80 kg and the median was 8.60 kg.

The distribution was right-skewed, with fewer observations at higher weights.

Canine patients showed substantially greater weight variability than feline patients.

---

## 7. Radiology Workload

Most examinations involved one or two radiographs.

Two-radiograph examinations were the most common, with 362 cases.

The average number of radiographs per examination was 1.66 and the median was 2.

A total of 40 records had missing radiograph-count information.

---

## 8. Radiograph Volume by Species

A total of 1,083 radiographs were recorded among examinations with available radiograph-count information.

Canine patients accounted for 796 recorded radiographs, while feline patients accounted for 286.

The higher canine volume is consistent with the greater number of canine examinations in the dataset.

---

## 9. Medical Reports

Medical reports were recorded in 301 of 693 records (43.4%).

A total of 350 records (50.5%) were marked as having no medical report, while 42 records (6.1%) had missing report information.

The strongest operational pattern identified in the EDA was the relationship between radiograph count and medical report status.

Among examinations with one radiograph, only 2.78% had a recorded report.

For examinations with two radiographs, 76.54% had a recorded report.

For examinations with three radiographs, 82.35% had a recorded report.

All examinations with four, five or six radiographs had a recorded report, although these categories contained very few observations.

---

## 10. Referring Veterinarians

The radiology service received referrals from multiple veterinary professionals.

After standardization of clearly identifiable naming variants, ERWIN RESTREPO was the highest-volume referring veterinarian with 96 recorded cases, followed by ANIBAL GARCIA with 55 and JAIME VEGA with 50.

Among the highest-volume referring veterinarians, medical report rates varied substantially.

These percentages should be interpreted together with referral volume and missing report information.

---

## 11. Temporal Activity

The available dataset is heavily concentrated in 2022.

There were 3 recorded examinations in 2021 and 686 in 2022.

Because the years are not equally represented, they should not be interpreted as directly comparable full-year periods.

The highest monthly activity occurred in September 2022, with 83 recorded cases.

November and December followed with 76 and 69 cases respectively.

---

## 12. Age and Weight Relationship

The analysis included 471 patients with both age and weight information available.

The scatter plot did not show a strong linear relationship between age and weight across the entire dataset.

Species appeared to be a stronger factor differentiating patient weight, with feline patients concentrated at lower weights and canine patients showing substantially wider variation.

---

## Main Operational Insights

The exploratory analysis suggests three particularly relevant areas for future monitoring:

### 1. Radiograph Count and Report Generation

The presence of a medical report was much more frequent in examinations involving two or more radiographs than in examinations involving a single radiograph.

### 2. Referral Network

A relatively small group of referring veterinarians contributed a substantial portion of the recorded referral volume.

### 3. Service Workload

Canine patients generated the majority of examinations and radiographic volume, while monthly activity varied considerably across the available study period.

These findings provide the analytical foundation for the future Streamlit dashboard.