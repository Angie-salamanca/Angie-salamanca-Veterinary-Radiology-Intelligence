-- ==========================================
-- VETERINARY RADIOLOGY INTELLIGENCE
-- SQL ANALYSIS
-- ==========================================


-- ==========================================
-- 1. MEDICAL REPORT RATE BY RADIOGRAPH COUNT
-- ==========================================

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
    ) AS missing_report,

    ROUND(
        COUNT(*) FILTER (
            WHERE medical_report = 'SI'
        )::numeric
        / NULLIF(
            COUNT(*) FILTER (
                WHERE medical_report IN ('SI', 'NO')
            ),
            0
        ) * 100,
        2
    ) AS report_rate_percentage

FROM public.radiology

GROUP BY radiograph_count

ORDER BY radiograph_count;


-- ==========================================
-- 2. MEDICAL REPORT RATE BY SPECIES
-- ==========================================

SELECT
    species,
    COUNT(*) AS total_cases,

    COUNT(*) FILTER (
        WHERE medical_report = 'SI'
    ) AS reports,

    COUNT(*) FILTER (
        WHERE medical_report = 'NO'
    ) AS no_reports,

    COUNT(*) FILTER (
        WHERE medical_report IS NULL
    ) AS missing_report,

    ROUND(
        COUNT(*) FILTER (
            WHERE medical_report = 'SI'
        )::numeric
        / NULLIF(
            COUNT(*) FILTER (
                WHERE medical_report IN ('SI', 'NO')
            ),
            0
        ) * 100,
        2
    ) AS report_rate_percentage

FROM public.radiology

GROUP BY species

ORDER BY total_cases DESC;


-- ==========================================
-- 3. CASES BY REFERRING VETERINARIAN
-- ==========================================

SELECT
    referring_veterinarian,
    COUNT(*) AS total_cases

FROM public.radiology

WHERE referring_veterinarian IS NOT NULL

GROUP BY referring_veterinarian

ORDER BY total_cases DESC;


-- ==========================================
-- 4. VETERINARIAN NAME VARIATIONS
-- ==========================================

SELECT
    UPPER(TRIM(referring_veterinarian)) AS veterinarian_name,
    COUNT(*) AS total_cases

FROM public.radiology

WHERE referring_veterinarian IS NOT NULL

GROUP BY UPPER(TRIM(referring_veterinarian))

ORDER BY total_cases DESC;


-- ==========================================
-- 5. TOP REFERRING VETERINARIANS AFTER
--    BASIC TEXT NORMALIZATION
-- ==========================================

SELECT
    UPPER(TRIM(referring_veterinarian)) AS veterinarian_name,
    COUNT(*) AS total_cases

FROM public.radiology

WHERE referring_veterinarian IS NOT NULL

GROUP BY UPPER(TRIM(referring_veterinarian))

ORDER BY total_cases DESC

LIMIT 15;


-- ==========================================
-- 6. STANDARDIZED REFERRING VETERINARIANS
-- ==========================================

SELECT
    CASE
        WHEN UPPER(TRIM(referring_veterinarian)) IN (
            'DR ERWIN RESTREPO',
            'ERWIN RETREPO',
            'ERWIN RETRESPO'
        )
        THEN 'ERWIN RESTREPO'

        WHEN UPPER(TRIM(referring_veterinarian)) IN (
            'DR JAIME VEGA',
            'JAI ME VEGA'
        )
        THEN 'JAIME VEGA'

        WHEN UPPER(TRIM(referring_veterinarian)) IN (
            'DR ANIBAL GARCIA',
            'DR ANIBAL'
        )
        THEN 'ANIBAL GARCIA'

        WHEN UPPER(TRIM(referring_veterinarian)) IN (
            'VET MATEOS',
            'MATEOS',
            'MAIRA GARCIA VET MATEOS',
            'JUAN CARLOS, MATEOS',
            'VETERINARIA MATEOS'
        )
        THEN 'MATEOS'

        WHEN UPPER(TRIM(referring_veterinarian)) = 'ANIBAL GARICIA'
        THEN 'ANIBAL GARCIA'

        ELSE UPPER(TRIM(referring_veterinarian))
    END AS veterinarian_standardized,

    COUNT(*) AS total_cases

FROM public.radiology

WHERE referring_veterinarian IS NOT NULL

GROUP BY
    CASE
        WHEN UPPER(TRIM(referring_veterinarian)) IN (
            'DR ERWIN RESTREPO',
            'ERWIN RETREPO',
            'ERWIN RETRESPO'
        )
        THEN 'ERWIN RESTREPO'

        WHEN UPPER(TRIM(referring_veterinarian)) IN (
            'DR JAIME VEGA',
            'JAI ME VEGA'
        )
        THEN 'JAIME VEGA'

        WHEN UPPER(TRIM(referring_veterinarian)) IN (
            'DR ANIBAL GARCIA',
            'DR ANIBAL'
        )
        THEN 'ANIBAL GARCIA'

        WHEN UPPER(TRIM(referring_veterinarian)) IN (
            'VET MATEOS',
            'MATEOS',
            'MAIRA GARCIA VET MATEOS',
            'JUAN CARLOS, MATEOS',
            'VETERINARIA MATEOS'
        )
        THEN 'MATEOS'

        WHEN UPPER(TRIM(referring_veterinarian)) = 'ANIBAL GARICIA'
        THEN 'ANIBAL GARCIA'

        ELSE UPPER(TRIM(referring_veterinarian))
    END

ORDER BY total_cases DESC;

