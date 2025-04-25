import asyncio
import os
from dotenv import load_dotenv
from config.logger import logger
from py_clob_client.client import ClobClient
from py_clob_client.constants import POLYGON

# Construct the path to the .env file in the parent directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'keys.env')

# Load environment variables from the specified path
load_dotenv(dotenv_path)

private_key = os.getenv('PK')
host = "https://clob.polymarket.com"
chain_id = POLYGON

async def get_polymarket_markets():

    client = None
    try:
        client = ClobClient(host, key=private_key, chain_id=chain_id)
        print("Initialized Polymarket ClobClient.")

        sample = client.get_sampling_markets()
        #rint(sample)

    except Exception as e:
        print(f"An error occurred: {e}")

def test_run():
    logger.info('test run')

    client = None

    try:
        client = ClobClient(host, key=private_key, chain_id=chain_id)



    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    #asyncio.run(get_polymarket_markets())
    test_run()