""" Modulo exclusivo para invocar a função screenGrab()
implementada em outro modulo. Não alterar o conteúdo! """

import importlib
import quickGrab
import mouse
import startGame
import clearTables
import coordinates
import cook
import buyFood
import pixels
import respondOrders
import play
# from cook import *

def grab():
  importlib.reload(quickGrab)
  quickGrab.main()

def reloadModules():
  importlib.reload(quickGrab)
  importlib.reload(mouse)
  importlib.reload(startGame)
  importlib.reload(coordinates)
  importlib.reload(clearTables)
  importlib.reload(cook)
  importlib.reload(buyFood)
  importlib.reload(pixels)
  importlib.reload(respondOrders)
  importlib.reload(play)

  
if __name__ == '__main__':
    grab()