class Animation:
  def __init__(self, data: dict):
    self.id = data['id']
    self.name = data['name']
    self.startDate = data['startDate']
    self.finishDate = data['finishDate']