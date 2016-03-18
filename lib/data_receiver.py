import serial
import logging
import time
import sys

class DataReceiver(object):
  def __init__(self, data_holder):
    self._port = '/dev/ttyACM0'
    self._baud_rate = 9600
    self._data_holder = data_holder

  def process(self, name, delay):
    while 1:
      self._fetch()

      time.sleep(delay)

  def _fetch(self):
    try:
      ser = serial.Serial(self._port, self._baud_rate)
      ids = ser.readline().rstrip().split(':')

      logging.info('Received ids: {}'.format(ids))
      self._data_holder.set_data(ids)
    except:
      logging.exception(sys.exc_info())

