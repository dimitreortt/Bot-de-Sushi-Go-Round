class FoodStock():
  Shrimp = 5
  Rice = 10
  Nori = 10
  Roe = 10
  Salmon = 5
  Unagi = 5

  def __str__(self):
    return 'Shrimp = %d | Rice = %d | Nori = %d | Roe = %d | Salmon = %d | Unagi = %d' % \
       (self.Shrimp, self.Rice, self.Nori, self.Roe, self.Salmon, self.Unagi)

  def reset(self):
    self.Shrimp = 5
    self.Rice = 10
    self.Nori = 10
    self.Roe = 10
    self.Salmon = 5
    self.Unagi = 5

  def getStock(self):
    return {'Shrimp': self.Shrimp, 'Rice': self.Rice, 'Nori': self.Nori, 'Roe': self.Roe, 'Salmon': self.Salmon, 'Unagi': self.Unagi}
