import sqlalchemy
import pandas as pd

engine = sqlalchemy.create_engine(
    'postgresql://postgres:RB9j2ZPOb0hiICMr6f7q@34.93.223.34/staging')


def returnPlatformId(query: str):
    df = pd.read_sql(query, engine)
    if len(df) == 0:
        return None
    column = df.columns[0]
    return df[column][0]
