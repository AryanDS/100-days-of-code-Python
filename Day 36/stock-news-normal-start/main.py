import requests as req
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY="XMDDWJOIBMRVDUO2"
NEWS_API_KEY = "e3483e3accd24127ab20f3ba608390b9"

account_sid = "AC6b271361dcc327aea75cfc9c168f4eee"
auth_token = "474e23f5182bbbf8f6d899424f5d97a0"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response1 = req.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={STOCK_API_KEY}")
response1.raise_for_status()
data = response1.json()


#data is the json file
data = data["Time Series (Daily)"]

#list comprehension

data_list = [value for (_, value) in data.items()]
yesterday_data = data_list[0]
day_before_data = data_list[1]



yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price
daybefore_closing_price = day_before_data['4. close']
print(daybefore_closing_price)


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_diff = abs(float(daybefore_closing_price) - float(yesterday_closing_price))
print(positive_diff)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff_daybefore = (positive_diff/float(yesterday_closing_price))*100
print(percentage_diff_daybefore)


#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
## STEP 2: https://newsapi.org/ 
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if percentage_diff_daybefore> 5:
    news_params={
        "apiKey": NEWS_API_KEY,
        "q":COMPANY_NAME

    }
    response2 = req.get(NEWS_ENDPOINT,params= news_params)
    response2.raise_for_status()
    data = response2.json()
    articles =  data['articles']

 


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
articles = articles[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

nl = '\n'
sms_articles = [f"Headline: {article['title']} {nl} Brief: {article['description']}" for article in articles]
print(sms_articles)
#TODO 9. - Send each article as a separate message via Twilio. 
client = Client(account_sid, auth_token)
for article in sms_articles:
    message = client.messages.create(
                                body=article,
                                from_='+13168006176',
                                to='+17169037801'
                            )        
    print(message.status)    



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

