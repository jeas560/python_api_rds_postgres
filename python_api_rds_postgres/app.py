from dotenv import dotenv_values
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

config = dotenv_values(".env")
key = config["API_KEY"]
url = config["URL"]


def get_data(start, limit, convert, key, url):
    parameters = {
        "start": start,
        "limit": limit,
        "convert": convert,
    }

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)

        coin_dict = {
            "name": [coin["name"] for coin in data["data"]],
            "symbol": [coin["symbol"] for coin in data["data"]],
            "date_added": [coin["date_added"] for coin in data["data"]],
            "last_updated": [coin["last_updated"] for coin in data["data"]],
            "price": [coin["quote"][convert]["price"] for coin in data["data"]],
            "volume_24h": [
                coin["quote"][convert]["volume_24h"] for coin in data["data"]
            ],
        }
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f"Error to get data from API: {e}")
        exit(1)

    coins_df = pd.DataFrame(
        coin_dict,
        columns=coin_dict.keys(),
    )
    print("Data on Pandas Dataframe:\n")
    print(coins_df.head())


get_data("1", "10", "USD", key, url)
