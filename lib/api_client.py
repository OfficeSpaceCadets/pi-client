import requests
import json

class ApiClient(object):
  def __init__(self):
    self._urL = 'https://osc-backend.herokuapp.com/api/ping'
    self._api_token = '24ee441f6823271610ea6c4e57d8541b'

    self._headers = {
        'Authorization': 'Token token={}'.format(self._api_token),
        'Content-Type': 'application/json'
      }
    
  def send_data(self, data):
    resp = requests.post(self._url, 
      data=json.dumps({ "ids": data }),
      headers=self._headers)

    if resp.status_code > 201:
      message = 'Failure! attempting to hit: {} with {} but got a {}'.format(self._url, ping, resp.status_code)
      raise Exception(message)

