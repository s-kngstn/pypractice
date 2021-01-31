import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "YQF4V3G13ZH0R3BT"
NEWS_API_KEY = "04ae6798863649828cbfc0411c689b4f"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list  = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterdays_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

diff = abs(float(yesterdays_closing_price) - float(day_before_yesterday_closing_price))

diff_percent = (diff / float(yesterdays_closing_price)) * 100


if diff_percent > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, news_params)
    articles = news_response.json()["articles"]
    top_three_articles = articles[:3]

    formatted_articles = [f"Headline {article['title']}. \nBrief: {article['description']}" for article in top_three_articles]

    print(formatted_articles[0])