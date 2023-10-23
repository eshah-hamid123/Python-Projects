from flask import Flask, render_template
app = Flask(__name__)


@app.route('/blog')
def home_page():
    #after file name you can give as many keyword arguements
    return render_template("further.html")


if __name__ == "__main__":
    app.run(debug=True)

#by adding code between these brackets {{ }} code gets evaluated as python code