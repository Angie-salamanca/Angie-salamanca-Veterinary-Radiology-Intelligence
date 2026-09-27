import pandas as pd


def load_clean_data():
    return pd.read_csv("data/processed/radiology_clean.csv")


def test_dataset_is_not_empty():
    df = load_clean_data()
    assert len(df) > 0


def test_expected_columns_exist():
    df = load_clean_data()
    expected_columns = [
        "patient_name",
        "species",
        "breed",
        "exam_date",
        "radiograph_count",
        "medical_report",
    ]
    for column in expected_columns:
        assert column in df.columns


def test_species_has_no_unexpected_values():
    df = load_clean_data()
    valid_species = {"CANINO", "FELINO", "CONEJO"}
    actual_species = set(df["species"].dropna().unique())
    assert actual_species.issubset(valid_species)


def test_radiograph_count_is_non_negative():
    df = load_clean_data()
    assert (df["radiograph_count"].dropna() >= 0).all()