import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st

from analysis import (
    get_cases_by_year,
    get_data_quality_metrics,
    get_report_by_radiograph_data,
    get_species_data,
)

from visualizations import (
    plot_cases_by_year,
    plot_report_rate_by_radiograph,
    plot_species_cases,
)


st.set_page_config(
    page_title="Veterinary Radiology Intelligence",
    page_icon="🩻",
    layout="wide",
)


st.title("Veterinary Radiology Intelligence")

st.write(
    "Análisis de estudios de radiología veterinaria "
    "utilizando PostgreSQL, Python y Plotly."
)


password = st.secrets["postgres_password"]

db_config = {
    "username": st.secrets["postgres_username"],
    "host": st.secrets["postgres_host"],
    "port": st.secrets.get("postgres_port", 5432),
    "database": st.secrets["postgres_database"],
    "sslmode": st.secrets.get("postgres_sslmode", "require"),
}


# Datos que NO se filtran por año
year_df = get_cases_by_year(password, db_config=db_config)
quality_df = get_data_quality_metrics(password, db_config=db_config)


# --- Filtro en la barra lateral ---
available_years = year_df["year"].dropna().astype(int)

min_year = int(available_years.min())
max_year = int(available_years.max())

st.sidebar.header("Filtros")

start_year, end_year = st.sidebar.slider(
    "Rango de años",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
)


# Datos que SÍ se filtran según el slider
species_df = get_species_data(password, start_year, end_year, db_config=db_config)

report_df = get_report_by_radiograph_data(password, start_year, end_year, db_config=db_config)


# --- KPIs (siempre sobre el dataset completo) ---
total_records = int(
    quality_df.loc[0, "total_records"]
)

records_with_date = int(
    quality_df.loc[0, "records_with_date"]
)

missing_dates = int(
    quality_df.loc[0, "missing_dates"]
)

missing_species = int(
    quality_df.loc[0, "missing_species"]
)


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Estudios totales",
        total_records
    )


with col2:
    st.metric(
        "Estudios con fecha",
        records_with_date
    )


with col3:
    st.metric(
        "Fechas faltantes",
        missing_dates
    )


with col4:
    st.metric(
        "Especies faltantes",
        missing_species
    )


st.subheader("Casos de radiología por especie")
st.caption(f"Mostrando años {start_year}–{end_year}")

st.plotly_chart(
    plot_species_cases(species_df),
    use_container_width=True,
)


st.subheader(
    "Tasa de informes según cantidad de radiografías"
)
st.caption(f"Mostrando años {start_year}–{end_year}")

st.plotly_chart(
    plot_report_rate_by_radiograph(report_df),
    use_container_width=True,
)


st.subheader("Casos de radiología por año")
st.caption("Vista completa, sin filtro")

st.plotly_chart(
    plot_cases_by_year(year_df),
    use_container_width=True,
)