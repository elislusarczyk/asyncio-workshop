import os
import uvloop
import logging
import asyncio

import pandas as pd


assert os.environ['GOOGLE_APPLICATION_CREDENTIALS']

logging.basicConfig(level=logging.DEBUG)

uvloop.install()


async def main():
    for offset in range(100, 400, 100):
        query = f'SELECT * FROM `riseupbi-prep.stage_wc.all_products` LIMIT 100 OFFSET {offset}'
        df = pd.read_gbq(query=query)
        print(df)


asyncio.run(main())