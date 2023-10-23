from flask import Flask, render_template, request
import requests
from smtplib import SMTP

my_email = 'eishahamid02@gmail.com'
password = 'wlixjefinseybbnd'

personal_email = 'eshahhamid02@gmail.com'


app = Flask(__name__)


@app.route('/')
def home_page():
    blog_url = " https://api.npoint.io/a71c04dfe4a887b04083"
    response = requests.get(blog_url)
    data = response.json()
    return render_template("index.html", posts=data)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'GET':
        return render_template("contact.html", method='GET')
    if request.method == 'POST':
        username = request.form['name']
        user_email = request.form['email']
        phone_number = request.form['phone']
        user_message = request.form['message']
        message_body = f'Username: {username}\n Email: {user_email} \n Contact Number: {phone_number} \n Message: {user_message}'
        with SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=personal_email,
                                msg=f'subject:Contact Info\n\n{message_body}')
        return render_template("contact.html", method='POST')


@app.route('/post/<num>')
def post_blog(num):
    num = int(num)
    blog_url = " https://api.npoint.io/442b950a53fff9d93a1c"
    response = requests.get(blog_url)
    data = response.json()
    return render_template("post.html", all_blogs=data, id=num)


if __name__ == "__main__":
    app.run(debug=True)

#by adding code between these brackets {{ }} code gets evaluated as python code

