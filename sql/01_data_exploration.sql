-- ==========================================
-- VETERINARY RADIOLOGY INTELLIGENCE
-- SQL DATA EXPLORATION
-- ==========================================


-- ==========================================
-- 1. VIEW SAMPLE RECORDS
-- ==========================================

SELECT *
FROM public.radiology
LIMIT 10;


-- ==========================================
-- 2. COUNT TOTAL RECORDS
-- ==========================================

SELECT COUNT(*) AS total_records
FROM public.radiology;

-- ==========================================
-- 3. SPECIES DISTRIBUTION
-- ==========================================

SELECT
    species,
    COUNT(*) AS cases
FROM public.radiology
GROUP BY species
ORDER BY cases DESC;


-- ==========================================
-- 4. CASES BY YEAR
-- ==========================================

SELECT
    EXTRACT(YEAR FROM exam_date) AS exam_year,
    COUNT(*) AS cases
FROM public.radiology
WHERE exam_date IS NOT NULL
GROUP BY EXTRACT(YEAR FROM exam_date)
ORDER BY exam_year;

-- ==========================================
-- 5. RADIOGRAPH COUNT DISTRIBUTION
-- ==========================================

SELECT
    radiograph_count,
    COUNT(*) AS cases
FROM public.radiology
GROUP BY radiograph_count
ORDER BY radiograph_count;

-- ==========================================
-- 6. MEDICAL REPORT STATUS
-- ==========================================

SELECT
    medical_report,
    COUNT(*) AS cases
FROM public.radiology
GROUP BY medical_report
ORDER BY cases DESC;

