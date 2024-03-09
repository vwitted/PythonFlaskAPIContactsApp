from flask import Flask, json,request
import pymongo
import json

app = Flask(__name__) 
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.Phonebook.Contacts

@app.route('/phonebook/<id>', methods=['GET'])
def get_phonebook(id):
    result = client.Phonebook.Contacts.find_one({'id':int(id)})
    return str(result)

@app.route("/phonebookID")
def get_phonebookID():
    id = request.args.get('id')
    result = client.Phonebook.Contacts.find_one({'id':int(id)})
    return str(result)

app.run()