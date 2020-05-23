from quickGrab import grabBubbleBox
from cook import makeFood
from buyFood import checkFood
import time

class BlankSeatsColorSum():
  Seat1 = 6832
  Seat2 = 5476
  Seat3 = 10073
  Seat4 = 10254
  Seat5 = 6581
  Seat6 = 8193

class OrdersColorSum():
  Onigiri = 2518
  Gunkan = 2524
  Caliroll = 2992

def checkOrderOnTable(i):
  rgbSum = grabBubbleBox(i)
  if rgbSum == OrdersColorSum.Onigiri:
    makeFood('onigiri')
  
  elif rgbSum == OrdersColorSum.Caliroll:
    makeFood('caliroll')
  
  elif rgbSum == OrdersColorSum.Gunkan:
    makeFood('gunkan')

  else:
    print('Error in checkOrder! No match found!')

def checkOrders():
  for i in range(1,7):    
    checkOrderOnTable(i)  
    if i == 2 or i == 4:
      checkFood()

  time.sleep(1.5)