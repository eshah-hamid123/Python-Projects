from smtplib import *

my_email = 'eishahamid02@gmail.com'
password = 'wlixjefinseybbnd'
with SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs='pareesay@yahoo.com', msg='subject:Hello\n\nThis is the body of my email')



