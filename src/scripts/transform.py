from venv import logger

import pandas as pd


def transform(df):
    """ Transform the DataFrame by filling missing values, creating andrenaming columns """
    
    logger.info("Starting data transformation...")
    df.fillna(0, inplace=True)
    df = df.rename(columns={'Class': 'suspeita'})
    df['suspeita'] = df['suspeita'] == 1
    HIGH_AMOUNT_THRESHOLD = 1000
    total = df['suspeita'].sum()
    logger.info("Transformation completed.")
    return df

