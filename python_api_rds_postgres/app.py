from dotenv import dotenv_values
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

from model import Coins

config = dotenv_values("../.env.development")
key = config["API_KEY"]
url = config["URL"]


def check_if_valid_data(df: pd.DataFrame) -> bool:
    if df.empty:
        print("\nDataframe empty. Finishing execution")
        return False

    if df.symbol.empty:
        raise Exception("\nSymbol is Null or the value is empty")

    if df.price.empty:
        raise Exception("\nPrice is Null or the value is empty")

    if df.date_added.empty:
        raise Exception("\nDate is Null or the value is empty")

    return True


def load_data(table_name, coins_df, session_db, engine_db):
    if check_if_valid_data(coins_df):
        print("\nData valid, proceed to Load stage")

    try:
        coins_df.to_sql(table_name, engine_db, index=False, if_exists="append")
        print("\nData Loaded on Database")
    except ValueError as e:
        print(f"\nFail to load data on database, Error: {e}")

    session_db.commit()
    session_db.close()
    print("\nClose database successfully")
    return session_db


def get_data(session_db, engine_db, start, limit, convert, key, url):
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

    load_data("Coins", coins_df, session_db, engine_db)


get_session_db, get_engine = Coins.start()

get_data(get_session_db, get_engine, "1", "10", "USD", key, url)
