import pandas as pd

from database import create_database_engine


engine = create_database_engine()


test_query = """
SELECT
    COUNT(*) AS total_records
FROM public.radiology;
"""


test_df = pd.read_sql(
    test_query,
    engine
)


print(test_df)


engine.dispose()