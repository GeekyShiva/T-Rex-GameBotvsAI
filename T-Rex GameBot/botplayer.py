## Works for split-screens, if you wnat to make changes do supply the marker position to replayBtn
# A value of 150 is highly optimised for the bot rather than any other value, but you may try diffrent values depending on your screensize
# This is a simple Chrome Dinasaur Inspired GameBot which runs well with http://www.trex-game.skipser.com/



from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    dinasaur = {234,471}
#   ducking Cordinatesx = 250
#   ducking Cordinatesy = 502
#   replayBtn = {532,464}
#   240 =  for x
#   y cordinate = 420

def restartGame():
   pyautogui.click(532,464)
   pyautogui.keyDown('down')


def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jump")
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')


def ImageGrab():
    box = (Cordinates.dinasaur[0] + 60, Cordinates.dinasaur[1], Cordinates.dinasaur[0]+150, Cordinates.dinasaur[1]+5)
    image = ImageGrab().grab(box)
    greyImage = ImageOps.grayscale(image)
    a = array(greyImage.getcolors())
    print(a.sum())
    return a.sum()


def main():
    restartGame()
    while True:
        if(ImageGrab()!=597):                   #You need to determine this value for your screensize
            pressSpace()                        # initial sum was 1447
            time.sleep(0.1)

while True:
    ImageGrab()


#print(pyautogui.size())
#print(pyautogui.position())
