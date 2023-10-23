from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/blog<num>')
def get_blog(num):
    blog_url = " https://api.npoint.io/442b950a53fff9d93a1c"
    response = requests.get(blog_url)
    data = response.json()
    #after file name you can give as many keyword arguements
    return render_template("index.html", posts=data)


if __name__ == "__main__":
    app.run(debug=True)

#by adding code between these brackets {{ }} code gets evaluated as python code