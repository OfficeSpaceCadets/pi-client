import requests

resp = requests.get('http://localhost:3000/api/ping')
if resp.status_code != 200:
  raise ApiError('Failure! {}'.format(resp.status_code))

for item in resp.json():
  print '{} {} {}'.format(item['id'], item['start_time'], item['end_time'])

