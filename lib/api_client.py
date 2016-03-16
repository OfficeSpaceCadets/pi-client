import requests
import json

class ApiClient(object):
  def __init__(self, url, api_token):
    self._url = url
    self._api_token = api_token
    
  def send_data(self, data):
    ping = { 'ids': data }
    resp = requests.post(self._url, data=ping,
      headers={ 'Authorization': 'Token token={}'.format(self._api_token) })
    if resp.status_code != 200:
      raise Exception('Failure! attempting to hit: {} with {} but got a {}'.format(self._url, ping, resp.status_code))

