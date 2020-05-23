from coordinates import Coords
from mouse import leftClick, setMousePos
from foodStock import FoodStock
import time

'''
Recipes:
 
    onigiri
        2 rice, 1 nori
     
    caliroll:
        1 rice, 1 nori, 1 roe
         
    gunkan:
        1 rice, 1 nori, 2 roe
'''

cds = Coords()

def clickRice():
  setMousePos(cds.f_Rice)
  leftClick()
  FoodStock.Rice -= 1

def clickRoe():
  setMousePos(cds.f_Roe)
  leftClick()
  FoodStock.Roe -= 1

def clickNori():
  setMousePos(cds.f_Nori)
  leftClick()
  FoodStock.Nori -= 1

def makeCaliroll():
  clickRice()
  clickNori()
  clickRoe()

def makeOnigiri():
  clickRice()
  clickRice()
  clickNori()

def makeGunkan():
  clickRice()
  clickNori()
  clickRoe()
  clickRoe()

def foldMat():
  x, y = cds.f_Rice
  setMousePos((x + 50, y))
  leftClick()
  time.sleep(1.5)

def makeFood(food):
  if food == 'caliroll':
    makeCaliroll()

  elif food == 'onigiri':
    makeOnigiri()
  
  elif food == 'gunkan':
    makeGunkan()
  
  foldMat()  
  
def cookDefautDishesAtTheBeggining():
  makeFood('caliroll')
  makeFood('gunkan')
  makeFood('onigiri')
  makeFood('onigiri')
  makeFood('caliroll')
  makeFood('caliroll')
  makeFood('caliroll')
  makeFood('gunkan')
