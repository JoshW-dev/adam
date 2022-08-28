import os
import time
import pyautogui



def moveto(xcord, ycord, dur):
    pyautogui.moveTo(xcord, ycord, duration=dur, tween=pyautogui.easeInOutQuad)
        
def click():
    pyautogui.click()

def typeCharacters(string):
    pyautogui.write(string, interval=0.15)

def presskey(keyName):
    pyautogui.press(keyName)

def hotkey():
    pyautogui.hotkey('alt', 'tab') 

def wait(sleeptime):
    time.sleep(sleeptime)

print("start")
wait(2)
#move to discord chat line
moveto(650,1055,1)
#move to discord chat line
click()
typeCharacters("/imagine")
presskey("enter")
wait(0.1)
typeCharacters("A beautiful painting")
wait(0.1)
presskey("enter")

print("end")

