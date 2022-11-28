from flask import Blueprint
import boto3
import json

author_api = Blueprint('author_api', __name__)

def getDataJson():
    s3 = boto3.resource('s3'
      # ACCESS_KEY
      # SECRET_KEY
    )
    content_object = s3.Object('pursuittrainings3', 'data.json')
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    return json_content

@author_api.route("/")
def bookList() -> list[object]:
    data = getDataJson()
    books = data['books']

    authors = set(map(lambda book: book['author'], books))
    
    return list(authors)