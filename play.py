from respondOrders import checkOrders
from buyFood import checkFood
from clearTables import clearTables
from startGame import startGame

def play():
  startGame()
  while True:
    checkOrders()
    checkFood()
    clearTables()