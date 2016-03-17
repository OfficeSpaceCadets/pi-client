import sys
import time
import logging

from api_client import ApiClient
from id_provider import IdProvider

class DataProcessor(object):
  def __init__(self):
    self._api_client = ApiClient()
    self._id_provider = IdProvider()

  def process(self, thread_name, delay):
    while 1:
      time.sleep(delay)
      logging.info('Processing input...')

      try:
        self._handle_input()
      except:
        logging.exception(sys.exc_info())
        
  def _handle_input(self):
    ids = self._id_provider.fetch_ids()
    logging.info('Received ids: {}'.format(ids))

    if len(ids) > 0:
      self._api_client.send_data(ids)

