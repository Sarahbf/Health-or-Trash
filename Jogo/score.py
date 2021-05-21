class Score:
  def __init__(self, total):
    self.total = total

  def sum_health_food(self):
    self.total += 10
  
  def sum_unhealth_food(self):
    self.total -= 20
  
  def reset(self):
    self.total = 0