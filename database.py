from getpass import getpass

from sqlalchemy import create_engine


def create_database_engine(
    password=None,
    username="postgres",
    host="localhost",
    port=5432,
    database="veterinary_radiology",
    sslmode="prefer",
):
    if password is None:
        password = getpass(
            "Contraseña de PostgreSQL: "
        )

    engine = create_engine(
        f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
        f"?sslmode={sslmode}"
    )

    return engine