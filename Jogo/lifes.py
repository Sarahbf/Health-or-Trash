class Lifes:
  def __init__(self, quantity):
    self.quantity = quantity
  
  def decrease(self):
    self.quantity -= 1
  
  def reset(self, quantity):
    self.quantity = quantity