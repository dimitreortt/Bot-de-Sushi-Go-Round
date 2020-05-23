from numpy import *
import PIL.ImageOps
from quickGrab import screenGrab
from coordinates import Coords

class FoodOrderPixels():
  RiceAvailable = (255, 255, 255)
  RiceUnavailable = (127,127,127)
  NoriAvailable = (66, 61, 22)
  NoriUnavailable = (33, 30, 11)
  RoeAvailable = (255, 122, 0)
  RoeUnavailable = (127, 61, 0)

def compareRiceOrderPixels():
  im = screenGrab()
  ricePixel = im.getpixel(Coords.t_Rice)

  if ricePixel == FoodOrderPixels.RiceAvailable:
    return True

  elif ricePixel == FoodOrderPixels.RiceUnavailable:
    return False  

  else:    
    print('Unknown pixelcolor at rice!!')
    print('Pixel received: ', ricePixel)

def compareNoriOrderPixels():
  im = screenGrab()
  noriPixel = im.getpixel(Coords.t_Nori)

  if noriPixel == FoodOrderPixels.NoriAvailable:
    return True

  elif noriPixel == FoodOrderPixels.NoriUnavailable:
    return False  

  else:    
    print('Unknown pixelcolor at nori!!')
    print('Pixel received: ', noriPixel)

def compareRoeOrderPixels():
  im = screenGrab()
  roePixel = im.getpixel(Coords.t_Roe)

  if roePixel == FoodOrderPixels.RoeAvailable:
    return True

  elif roePixel == FoodOrderPixels.RoeUnavailable:
    return False  

  else:    
    print('Unknown pixelcolor at Roe!!')
    print('Pixel received: ', roePixel)

# print(compareRoeOrderPixels())