import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

news_API_key = "1b2f1cd548744489b3c51519d5f854ff"
news_endpoint = 'https://newsapi.org/v2/everything'

stock_endpoint = 'https://www.alphavantage.co/query'
stock_API_key = 'CIW63UUS70MX3IDX'

news_parameters = {
    'apiKey': news_API_key,
    'qInTitle': COMPANY_NAME,
}

auth_token = '640cf88cb5b55ea6d6d1463da3c14843'
account_sid = 'AC90c30b099dbb4b41efa06e099bb3dab8'


parameters = {
    'lat': 31.520370,
    'lon': 74.358749,
    'appid': '7b4018440c66c3aae48ca2ec3a7bb4f0',
    'exclude': 'current,minutely,daily'
}

stock_news_parameters = {
    'symbol': STOCK,
    'function': 'TIME_SERIES_DAILY',
    'apikey': stock_API_key,
}

stock_response = requests.get(url=stock_endpoint, params=stock_news_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
daily_data = stock_data['Time Series (Daily)']
# print(stock_data)
data_list = [value for (key,value) in daily_data.items()]

yesterday_profit = float(data_list[0]['4. close'])
day_bef_yes_prof = float(data_list[1]['4. close'])

diff = day_bef_yes_prof - yesterday_profit
# diff = abs(diff)

up_down = None
if diff > 0:
    up_down = 'Up'

else:
    up_down = 'Down'

diff_percent = round(diff / yesterday_profit * 100)

if abs(diff_percent) > 5:
    news_response = requests.get(url=news_endpoint, params=news_parameters)
    news_response.raise_for_status()
    data = news_response.json()['articles']
    three_articles = data[:3]


    for article in three_articles:
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"{STOCK} : {up_down} {int(diff_percent)}% \n Headline: {article['title']} \n Brief: {article['description']}",
            from_='+19805505811',
            to='+923224381967'
        )
        print(message.status)



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

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

