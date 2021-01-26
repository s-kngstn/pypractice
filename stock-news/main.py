import requests
import datetime

class Percent(float):
    def __str__(self):
        return '{:.2%}'.format(self)

def percent_diff(old_value, new_value):
    diff = (new_value - old_value) / (old_value)
    return diff

STOCK = "GME"
COMPANY_NAME = "Tesla Inc"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

today = datetime.date.today()
day = today.weekday()
STOCK_API_KEY = "YQF4V3G13ZH0R3BT"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()

if day < 5:
    # Dates
    yesterday = str(today - datetime.timedelta(days=1))
    two_days_ago = str(today - datetime.timedelta(days=2))
    three_days_ago = str(today - datetime.timedelta(days=3))
    four_days_ago = str(today - datetime.timedelta(days=4))
    # Monday
    if day == 0:
        last_friday_price = float(stock_data["Time Series (Daily)"][three_days_ago]['5. adjusted close'])
        last_thursday_price = float(stock_data["Time Series (Daily)"][four_days_ago]['5. adjusted close'])
        percent_change = Percent(percent_diff(last_thursday_price, last_friday_price))
    # Tuesday
    elif day == 1:
        last_friday_price = float(stock_data["Time Series (Daily)"][four_days_ago]['5. adjusted close'])
        yesterdays_price =  float(stock_data["Time Series (Daily)"][yesterday]['5. adjusted close'])
        percent_change = Percent(percent_diff(last_friday_price, yesterdays_price))
    # Wed, Thur, Friday
    else:
        two_days_ago_price = float(stock_data["Time Series (Daily)"][two_days_ago]['5. adjusted close'])
        yesterdays_price = float(stock_data["Time Series (Daily)"][yesterday]['5. adjusted close'])
        percent_change = Percent(percent_diff(two_days_ago_price, yesterdays_price))

    print(percent_change)
    percent_change = float(percent_change)

    if percent_change > 0.05 or percent_change < -0.05:
        print("GET NEWS")
    else:
        print("normal swings")
else: 
    print("Weekend, Markets Closed")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

