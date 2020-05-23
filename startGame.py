from mouse import *
from coordinates import ButtonsCoords
from cook import cookDefautDishesAtTheBeggining
from foodStock import FoodStock

coords = ButtonsCoords()

def clickPlay():
  print(coords.Play)
  setMousePos(coords.Play)
  leftClick()

def clickContinue():
  setMousePos(coords.Continue)
  leftClick()

def clickSkip():
  setMousePos(coords.Skip)
  leftClick()

def clickSecondContinue():
  setMousePos(coords.TodaysGoalContinue)
  leftClick()

# Deve estar com a tela inicial
# e na posição certa
def startGame():
  clickPlay()
  clickContinue()
  clickSkip()
  clickSecondContinue()
  FoodStock().reset()
  # cookDefautDishesAtTheBeggining()
