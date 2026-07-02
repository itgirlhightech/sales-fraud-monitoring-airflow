from asyncio.log import logger
import os
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine


def load(df):
    """Load the DataFrame into a PostgreSQL database."""

    load_dotenv()

    logger.info("Loading data into PostgreSQL...")
    
    engine = create_engine(
        f"postgresql+psycopg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )

    df.to_sql(
        name="transactions",
        con=engine,
        if_exists="replace",
        index=False
    )

    logger.info("Data loaded successfully.")