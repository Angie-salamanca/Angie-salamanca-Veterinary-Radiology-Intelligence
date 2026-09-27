SPECIES_QUERY = """
SELECT
    species,
    COUNT(*) AS total_cases
FROM public.radiology
WHERE EXTRACT(YEAR FROM exam_date) BETWEEN :start_year AND :end_year
GROUP BY species
ORDER BY total_cases DESC;
"""


REPORT_BY_RADIOGRAPH_QUERY = """
SELECT
    radiograph_count,
    COUNT(*) AS total_cases,

    COUNT(*) FILTER (
        WHERE medical_report = 'SI'
    ) AS reports,

    COUNT(*) FILTER (
        WHERE medical_report = 'NO'
    ) AS no_reports,

    COUNT(*) FILTER (
        WHERE medical_report IS NULL
    ) AS missing_report

FROM public.radiology
WHERE EXTRACT(YEAR FROM exam_date) BETWEEN :start_year AND :end_year
GROUP BY radiograph_count
ORDER BY radiograph_count;
"""


CASES_BY_YEAR_QUERY = """
SELECT
    EXTRACT(YEAR FROM exam_date) AS year,
    COUNT(*) AS total_cases
FROM public.radiology
WHERE exam_date IS NOT NULL
GROUP BY year
ORDER BY year;
"""

DATA_QUALITY_QUERY = """
SELECT
    COUNT(*) AS total_records,

    COUNT(exam_date) AS records_with_date,

    COUNT(*) - COUNT(exam_date) AS missing_dates,

    COUNT(species) AS records_with_species,

    COUNT(*) - COUNT(species) AS missing_species

FROM public.radiology;
"""