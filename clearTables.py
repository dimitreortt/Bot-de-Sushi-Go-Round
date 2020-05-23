from coordinates import PlatesCoords
from mouse import leftClick, setMousePos
import time 

def clearTables():
  pc = PlatesCoords()
  for seat in pc.SeatList:
    setMousePos(seat)
    leftClick()    
  
  time.sleep(1.5)

if __name__ == "__main__":
  clearTables()
  pass
# pc = PlatesCoords()
# print(pc.SeatList)