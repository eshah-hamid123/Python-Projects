import datetime as dt
import pandas
import random
from smtplib import SMTP
##################### Extra Hard Starting Project ######################
my_email = 'eishahamid02@gmail.com'
password = 'wlixjefinseybbnd'
PLACEHOLDER = '[NAME]'
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")
data = data.to_dict(orient="records")

now = dt.datetime.now()
for birthday in range(len(data)):
    if data[birthday]['year'] == now.year and data[birthday]['month'] == now.month and data[birthday]['day'] == now.day:
        file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter:
            content = letter.read()
            new_content = content.replace(PLACEHOLDER, data[birthday]['name'])

        with SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=data[birthday]['email'],
                                msg=f'subject:Happy Birthday\n\n{new_content}')
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




