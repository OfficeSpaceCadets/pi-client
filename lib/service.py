import logging
import thread
import sys

from data_sender import DataSender
from data_receiver import DataReceiver
from data_holder import DataHolder

class Service(object):
  def __init__(self):
    data_holder = DataHolder()
    self._data_sender = DataSender(data_holder)
    self._data_receiver = DataReceiver(data_holder)

  def main(self):
    logging.basicConfig(filename='/var/log/pi-client/pi-client.log', filemode='w', level=logging.DEBUG)

    logging.info('Processing input...')

    try:
      thread.start_new_thread(self._data_receiver.process, ('data receiver', 1))
      thread.start_new_thread(self._data_sender.process, ('data sender', 2))
    except:
      print "Unable to start thread", sys.exc_info()


