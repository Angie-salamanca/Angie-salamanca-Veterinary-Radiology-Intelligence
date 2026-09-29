import pandas as pd
from sqlalchemy import text

from database import create_database_engine
from queries import (
    SPECIES_QUERY,
    REPORT_BY_RADIOGRAPH_QUERY,
    CASES_BY_YEAR_QUERY,
    DATA_QUALITY_QUERY,
)


def get_species_data(password=None, start_year=None, end_year=None, db_config=None):
    engine = create_database_engine(password, **(db_config or {}))

    species_df = pd.read_sql(
        text(SPECIES_QUERY),
        engine,
        params={"start_year": start_year, "end_year": end_year},
    )

    engine.dispose()

    return species_df


def get_report_by_radiograph_data(password=None, start_year=None, end_year=None, db_config=None):
    engine = create_database_engine(password, **(db_config or {}))

    report_df = pd.read_sql(
        text(REPORT_BY_RADIOGRAPH_QUERY),
        engine,
        params={"start_year": start_year, "end_year": end_year},
    )

    engine.dispose()

    return report_df


def get_cases_by_year(password=None, db_config=None):
    engine = create_database_engine(password, **(db_config or {}))

    year_df = pd.read_sql(
        CASES_BY_YEAR_QUERY,
        engine
    )

    engine.dispose()

    return year_df


def get_data_quality_metrics(password=None, db_config=None):
    engine = create_database_engine(password, **(db_config or {}))

    quality_df = pd.read_sql(
        DATA_QUALITY_QUERY,
        engine
    )

    engine.dispose()

    return quality_df