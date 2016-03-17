import time

from api_client import ApiClient
from id_provider import IdProvider

class DataProcessor(object):
  def __init__(self):
    self._api_client = ApiClient()
    self._id_provider = IdProvider()

  def process(self, thread_name, delay):
    while 1:
      time.sleep(delay)

      self._handle_input()
        

  def _handle_input(self):
    ids = self._id_provider.fetch_ids()

    if len(ids) > 0:
      self._api_client.send_data(ids)

