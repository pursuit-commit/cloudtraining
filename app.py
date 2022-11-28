from flask import Flask
from books import book_api
from authors import author_api

app = Flask(__name__)

app.register_blueprint(book_api, url_prefix='/books')
app.register_blueprint(author_api, url_prefix='/authors')


@app.route("/")
def hello():
    return "Welcome to My Bookstore API!"

if __name__ == "__main__":
    app.run()