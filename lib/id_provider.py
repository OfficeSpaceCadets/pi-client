import serial

class IdProvider(object):
  def __init__(self):
    self._port = '/dev/ttyACM0'
    self._baud_rate = 9600

  def fetch_ids(self):
    ser = serial.Serial(self._port, self._baud_rate)
    line = ser.readline().rstrip()
    return line.split(':')


