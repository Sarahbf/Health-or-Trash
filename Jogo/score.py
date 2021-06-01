class Score:
  def __init__(self, total):
    self.total = total

  def sum_health_food(self):
    self.total += 10
  
  def sum_unhealth_food(self):
    if self.total <= 20:
      self.total = 0
    else:
      self.total -= 20
  
  def reset(self):
    self.total = 0