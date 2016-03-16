import serial
import requests
import thread
import time
import sys

from session_tracker import SessionTracker
from api_client import ApiClient

session_tracker = SessionTracker()

endpoint = 'http://osc-backend.herokuapp.com/api/ping'
api_token = '24ee441f6823271610ea6c4e57d8541b'

def fetch_data(thread_name, delay):
  ser = serial.Serial('/dev/ttyACM0', 9600)

  while 1:
    time.sleep(delay)
    line = ser.readLine()
    session_tracker.update(line.strip())

def report_data(thread_name, delay):
  api_client = ApiClient(endpoint, api_token)

  while 1:
    time.sleep(delay)
    api_client.send_data(session_tracker.get_ids())

try:
  thread.start_new_thread(fetch_data, ('fetch data', 500))
  thread.start_new_thread(report_data, ('report data', 1000))
except:
  print "Unable to start thread", sys.exc_info()

while 1:
  pass

