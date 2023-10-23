from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = " https://api.npoint.io/442b950a53fff9d93a1c"
    response = requests.get(blog_url)
    data = response.json()
    return render_template("index.html", posts=data)


@app.route('/post/<num>')
def post_blog(num):
    num = int(num)
    blog_url = " https://api.npoint.io/442b950a53fff9d93a1c"
    response = requests.get(blog_url)
    data = response.json()
    return render_template("post.html", all_blogs=data, id=num)


if __name__ == "__main__":
    app.run(debug=True)
