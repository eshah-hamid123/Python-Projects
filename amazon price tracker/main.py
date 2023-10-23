import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
import datetime as dt
URL = 'https://www.amazon.com/carson-colorblock-convertible-crossbody-Multi/dp/B09L7BYPZP/ref=sr_1_24?qid=1658151691&s=fashion-womens-intl-ship&sr=1-24'
AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
LANGUAGE = 'en-US,en;q=0.9'

my_email = 'eishahamid02@gmail.com'
password = 'wlixjefinseybbnd'

headers = {
    'User-Agent' : AGENT,
    'Accept-Language': LANGUAGE
}



response = requests.get(url=URL, headers=headers)
content = response.text


soup = BeautifulSoup(content, 'lxml')
price = soup.find(name='span', class_='a-offscreen').getText()
price_in_no = price.split('$')[1]
float_price = float(price_in_no)

title = soup.find(id='productTitle').getText().strip()
msg = f'Subject:Amazon Price Tracker\n\nInstant {title} is now ${float_price}.'

if float_price < 200:
    with SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='eshahhamid02@gmail.com',
                            msg=msg)
