""" 
All coordinates assume a screen resolution of 1366x768, and Chrome 
maximized without the Bookmarks Toolbar enabled.
Only the slightiest white lane was kept above the blue baloon
to center the play area in browser.
x_pad = 113
y_pad = 120
Play area =  x_pad+1, y_pad+1, 796, 825
"""
from PIL import ImageGrab
import os
import time
 
# Globals
x_pad = 113
y_pad = 120

def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 639, y_pad + 480)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    # screenGrab()
    pass
 
if __name__ == '__main__':
    main()