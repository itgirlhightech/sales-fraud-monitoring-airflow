from asyncio.log import logger

import pandas as pd

def extract():
    """ Load the CSV file into a pandas DataFrame """

    logger.info("Reading CSV file...")
    df = pd.read_csv('src/data/creditcard_sample_10000.csv')
    logger.info(f"{len(df)} records extracted.")
    return df


   