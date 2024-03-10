import os, json, requests
from twilio.rest import Client
from dotenv import find_dotenv, load_dotenv
import pandas as pd


dotenv_path = find_dotenv()
# print(dotenv_path)
load_dotenv(dotenv_path)

TRILIO_TOKEN = os.getenv("TRILIO_TOKEN")
TRILIO_SID = os.getenv("TRILIO_SID")
TRILIO_NUM = os.getenv("TRILIO_NUM")
POLYGON_API = os.getenv("POLYGON_API")


screener = pd.read_csv('data/nasdaq_screener_1706064383140.csv')
tickers = screener['Symbol'].tolist()


def market_refresh():

    market = []
    for x in tickers[:5]:
        polygon = requests.get(
            f'https://api.polygon.io/v2/aggs/ticker/{x}/range/1/day/2024-01-22/2024-01-23?apiKey={POLYGON_API}').json()
        market.append(polygon)

        tick = requests.get(f'''https://api.tickertick.com/feed?q=(and T:curated tt:{x})&n=1''').json()
        market.append(tick)

    with open(file='data/market_data', mode='w') as file:
        json.dump(market, file)


# with open(file='data/market_data', mode='r') as y:
#     records = pd.read_json(y)
#     print(records)
#
#     for x in records.iloc:
#         help_me = (x["ticker"], x["results"][0]["o"], x["results"][0]["c"])
#         print(help_me)


def send_sms():
    # TRILIO_TOKEN
    # TRILIO_SID

    account_sid = "ACbb711eddf65ad038333f8dee9447d530"
    auth_token = "4824dbef466b854e1dd9469b981ff41a"

    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to="+13529884510",
        from_=TRILIO_NUM,
        body="Hello"
    )


send_sms()
