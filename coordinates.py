""" 
## Buttons Coordinates: ##
Play: 324 205
Continue: 316 391
Skip: 585 454
Todays goal continue: 310 374
"""

class ButtonsCoords():
  Play = (324, 205)
  Continue = (316, 391)
  Skip = (585, 454)
  TodaysGoalContinue = (310, 374)


"""
## Foods Coordinates (prefix f_) ##
Shrimp = 40 333
Rice = 98 341
Nori = 33 384
Roe = 92 389
Salmon = 34 450
Unagi = 94 440
"""

"""
## Foods On The Telefone (prefix t_) ##
t_Shrimp = (491, 222)
t_Unagi = (576, 227)
t_Nori = (491, 278)
t_Roe = (577, 280)
t_Salmon = (491, 338)
"""
class Coords():
  # Food
  f_Shrimp = (40, 333)
  f_Rice = (98, 341)
  f_Nori = (33, 384)
  f_Roe = (92, 389)
  f_Salmon = (34, 450)
  f_Unagi = (94, 440)

  # Telephone Food
  t_Shrimp = (491, 222)
  t_Unagi = (576, 227)
  t_Nori = (491, 278)
  t_Roe = (577, 280)
  t_Salmon = (491, 338)
  t_Rice = (544, 281)

  # Telephone Options
  telephone = (582, 362)
  toppingOrder = (536, 271)
  riceOrder = (539, 296)
  freeDelivery = (491, 298)
  riceHangout = (584, 337)
  toppingHangout = (595, 335)
  
"""
## Plates Coordinates ##
Seat1 = 92 210
Seat2 = 195 210
Seat3 = 292 210
Seat4 = 395 205
Seat5 = 502 203
Seat6 = 602 210
"""
class PlatesCoords():
  Seat1 = (92, 210)
  Seat2 = (195, 210)
  Seat3 = (292, 210)
  Seat4 = (395, 210)
  Seat5 = (483, 210)
  Seat6 = (602, 210)

  SeatList = [Seat1, Seat2, Seat3, Seat4, Seat5, Seat6]

# if __name__ == "__main__":
#   pc = PlatesCoords()
#   print(pc.SeatList)