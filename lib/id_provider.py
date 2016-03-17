import serial

class IdProvider(object):

  def __init__(self):
    port = '/dev/ttyACM0'
    baud_rate = 9600
    self._ser = serial.Serial(port, baud_rate)

  def fetch_ids(self):
    line = self._ser.readline()
    return line.split(':')


