class Result:
  def __init__(self, title, value):
    self.title = title
    self.value = value

  def prettyprint(self):
    print self.title + ': ' + self.value
