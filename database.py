from getpass import getpass

from sqlalchemy import create_engine


def create_database_engine(password=None):
    username = "postgres"

    if password is None:
        password = getpass(
            "Contraseña de PostgreSQL: "
        )

    engine = create_engine(
        f"postgresql+psycopg2://{username}:{password}@localhost:5432/veterinary_radiology"
    )

    return engine