import requests
from twilio.rest import Client
from necessary_parameters import *


# required stock parameters
stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": Interval,
    "apikey": STOCK_API_KEY,
}

# get data from alpha vantage api
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()[f"Time Series ({Interval})"]
data_list = [value for (key, value) in data.items()]

# last closing stock price
last_data = data_list[0]
last_closing_price = last_data["4. close"]
print(last_closing_price)

# second last closing stock price
second_last_data = data_list[1]
second_last_closing_price = second_last_data["4. close"]
print(second_last_closing_price)

# difference between them
difference = float(last_closing_price) - float(second_last_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# difference percentage
diff_percent = round((difference / float(last_closing_price)) * 100)
print(diff_percent)


if abs(diff_percent) >= Intraday_diff:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    # access news articles about specified company using news api
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # create a list that contains the first 3 articles.
    three_articles = articles[:3]
    print(three_articles)

    # Create a new list of the first 3 article's headline and description
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for
        article in three_articles]
    print(formatted_articles)

    # Send each article as a separate message via Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )