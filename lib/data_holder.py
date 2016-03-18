class DataHolder(object):
  def __init__(self):
    self._ids = []

  def set_data(self, data):
    self._ids = data

  def get_data(self):
    return self._ids

