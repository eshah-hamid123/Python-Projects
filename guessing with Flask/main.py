import random

from flask import Flask, render_template
import requests
app = Flask(__name__)

age_param = {
    "name" : "Eisha"
}
headers = {
    "content-type": "application/json"
}
name = "Eisha"
response = requests.get(url=f"https://agify.io?name={name}", headers=headers)
print(response)
response.raise_for_status()
if response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json"):
    age_data = response.json()
    print(age_data)
else:
    print('Req failed')


@app.route('/<num>')
def home_page():
    random_no = random.randint(1, 10)
    #after file name you can give as many keyword arguements
    return render_template("index.html", num=random_no)


if __name__ == "__main__":
    app.run(debug=True)

#by adding code between these brackets {{ }} code gets evaluated as python code