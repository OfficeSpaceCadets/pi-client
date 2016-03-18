import requests
import json
import logging
import time
import sys

class DataSender(object):
  def __init__(self, data_holder):
    self._url = 'https://osc-backend.herokuapp.com/api/ping'
    # self._url = 'http://192.168.0.106:3000/api/ping'
    self._api_token = '24ee441f6823271610ea6c4e57d8541b'

    self._headers = {
        'Authorization': 'Token token={}'.format(self._api_token),
        'Content-Type': 'application/json'
      }
    self._data_holder = data_holder
    
  def process(self, name, delay):
    while 1:
      if len(self._data_holder.get_data()) > 0:
        self._send()

      time.sleep(delay)

  def _send(self):
    try:
      logging.info('Sending data...')

      ping = json.dumps({ "ids": self._data_holder.get_data() })
      resp = requests.post(self._url, 
        data=ping,
        headers=self._headers)

      if resp.status_code > 201:
        message = 'Failure! attempting to hit: {} with {} but got a {}'.format(self._url, ping, resp.status_code)
        logging.error(message)
      else:
        logging.info('Successfully sent to server')
    except:
      logging.exception(sys.exc_info())

