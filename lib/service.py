import logging
import thread
import sys

from data_processor import DataProcessor

class Service(object):
  def __init__(self):
    self._data_processor = DataProcessor()

  def main(self):
    logging.basicConfig(filename='/var/log/pi-client/pi-client.log', filemode='w', level=logging.DEBUG)

    try:
      thread.start_new_thread(self._data_processor.process, ('process_data', 1))
    except:
      print "Unable to start thread", sys.exc_info()


