from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return "This is a<h2>Home Page</h2> !!"


if __name__ == '__main__':
    app.run(debug=True)
