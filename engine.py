import sqlalchemy
import pandas as pd

# DATABASE_URL = "postgresql://postgres:RB9j2ZPOb0hiICMr6f7q@34.100.136.218/production_clone"
DATABASE_URL = "postgresql://postgres:RB9j2ZPOb0hiICMr6f7q@35.244.45.226/dev_clone"

engine = sqlalchemy.create_engine(DATABASE_URL)

def returnPlatformId(query: str):
    df = pd.read_sql(query, engine)
    if len(df) == 0:
        return None
    column = df.columns[0]
    return df[column][0]
