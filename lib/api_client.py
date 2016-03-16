
class ApiClient(object):
  def __init__(self, url, api_token):
    self._url = url
    self._api_token = api_token
    
  def send_data(self, data):
    ping = { 'ids': data }
    resp = requests.put(self._url, json=ping, 
      headers={ 'Authorization': 'Token token={}'.format(api_token) })
    if resp.status_code != 200:
      raise ApiError('Failure! {}'.format(resp.status_code))

