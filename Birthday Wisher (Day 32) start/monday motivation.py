import datetime as dt
from random import choice
from smtplib import *

my_email = 'eishahamid02@gmail.com'
password = 'wlixjefinseybbnd'

now = dt.datetime.now()

if now.weekday() == 0:
    with open("quotes.txt") as quote_file:
        content = quote_file.readlines()
        quote = choice(content)
    with SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f'Subject:Monday motivation\n\n{quote}')




