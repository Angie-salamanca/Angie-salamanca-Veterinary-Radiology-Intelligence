import plotly.express as px
import pandas as pd


def plot_species_cases(species_df):
    chart_df = species_df.dropna(
        subset=["species"]
    ).copy()

    fig = px.bar(
        chart_df,
        x="species",
        y="total_cases",
        title="Casos de radiología por especie",
        labels={
            "species": "Especie",
            "total_cases": "Número de casos",
        },
    )

    return fig


def plot_report_rate_by_radiograph(report_df):
    chart_df = report_df.dropna(
        subset=["radiograph_count"]
    ).copy()

    chart_df["report_rate_percentage"] = (
        chart_df["reports"]
        / (
            chart_df["reports"]
            + chart_df["no_reports"]
        )
        * 100
    ).round(2)

    fig = px.bar(
        chart_df,
        x="radiograph_count",
        y="report_rate_percentage",
        title="Tasa de informes según cantidad de radiografías",
        labels={
            "radiograph_count": "Cantidad de radiografías",
            "report_rate_percentage": "Tasa de informes (%)",
        },
    )

    return fig


def plot_cases_by_year(year_df):
    chart_df = year_df.copy()

    chart_df["year"] = (
        chart_df["year"]
        .astype(int)
        .astype(str)
    )

    fig = px.bar(
        chart_df,
        x="year",
        y="total_cases",
        text="total_cases",
        title="Casos de radiología por año",
        labels={
            "year": "Año",
            "total_cases": "Número de casos",
        },
    )

    fig.update_traces(
        textposition="outside"
    )

    return fig