
class SessionTracker(object):
  def __init__(self):
    self._ids = []

  def update(self, line):
    self._ids = line.split(':')

  def get_ids(self):
    return self._ids

