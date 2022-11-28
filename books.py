from flask import Blueprint
import json
import boto3

book_api = Blueprint('book_api', __name__)

def getDataJson():
    s3 = boto3.resource('s3'
      # ACCESS_KEY
      # SECRET_KEY
    )
    content_object = s3.Object('pursuittrainings3', 'data.json')
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    return json_content

@book_api.route("/")
def bookList() -> list[object]:
    data = getDataJson()
    books = data['books']
    return books

@book_api.route("/<int:id>")
def getBook(id: int) -> object:
    data = getDataJson()
    books = data['books']
    for book in books:
        if book['id'] == id:
            return book
    return "Book not found", 404