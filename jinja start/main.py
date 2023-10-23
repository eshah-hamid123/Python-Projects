from flask import Flask, render_template
import random
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def home_page():
    date = datetime.now()
    year = date.strftime("%Y")
    random_no = random.randint(1, 10)
    #after file name you can give as many keyword arguements
    return render_template("index.html", num=random_no, copyright_year=year)


if __name__ == "__main__":
    app.run(debug=True)

#by adding code between these brackets {{ }} code gets evaluated as python code