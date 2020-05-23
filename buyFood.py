from coordinates import Coords as cds
from mouse import setMousePos, leftClick
from foodStock import FoodStock
import pixels

def clickPhone():
  print(cds.telephone)
  setMousePos(cds.telephone)
  leftClick()
  pass

def clickToppingOrder():
  setMousePos(cds.toppingOrder)
  leftClick()

def clickBuyRoe():
  setMousePos(cds.t_Roe)
  leftClick()

def clickBuyNori():
  setMousePos(cds.t_Nori)
  leftClick()

def clickRiceOrder():
  setMousePos(cds.riceOrder)
  leftClick()

def clickBuyRice():
  setMousePos(cds.t_Rice)
  leftClick()

def clickFreeDelivery():
  setMousePos(cds.freeDelivery)
  leftClick()

def clickToppingHangout():
  setMousePos(cds.toppingHangout)
  leftClick()

def clickRiceHangout():
  setMousePos(cds.riceHangout)
  leftClick()

def affordable(food):
  if food == 'Rice':
    return pixels.compareRiceOrderPixels()

  elif food == 'Nori':
    return pixels.compareNoriOrderPixels()
    pass

  elif food == 'Roe':
    print('aki')
    return pixels.compareRoeOrderPixels()
    pass

  else:
    print('Erro em phone.py!!')

def buyRice():
  clickPhone()
  clickRiceOrder()
  if(affordable('Rice')):
    print('Rice is affordable!')
    clickBuyRice()
    clickFreeDelivery()
    FoodStock.Rice += 10
    print(FoodStock())
  else:
    clickRiceHangout()
    print('Rice is not affordable!')


def buyNori():
  clickPhone()
  clickToppingOrder()
  if(affordable('Nori')):    
    clickBuyNori()
    clickFreeDelivery()
    FoodStock.Nori += 10
    print(FoodStock())    
  else:
    clickToppingHangout()
    print('Nori is not affordable!') 

def buyRoe():
  clickPhone()
  clickToppingOrder()
  if(affordable('Roe')):
    clickBuyRoe()
    clickFreeDelivery()
    FoodStock.Roe += 10
    print('Bought Roe!', FoodStock())
  else:
    clickToppingHangout()
    print('Cant buy Roe!')

def buyFood(food):
  if food == 'Rice':
    buyRice()

  elif food == 'Nori':
    buyNori()

  elif food == 'Roe':
    buyRoe()

def checkFood():
  for i, j in FoodStock().getStock().items():
    if i == 'Nori' or i == 'Rice' or i == 'Roe':
      if j <= 4:
        print('%s is low and needs to be replenished' % i)
        buyFood(i)
      # print('%s is ok!' % i)