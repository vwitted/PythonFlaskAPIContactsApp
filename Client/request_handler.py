import requests
import json

class RequestHandler(object):
    
    def __init__(self):
        self.url = 'http://localhost:5000'

    def get_phonebook_data(self,id):
        resp = requests.get(self.url + '/phonebook/' + str(id))
        print(resp.text)
