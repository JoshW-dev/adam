import os
import time
import pyautogui


class commands:
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

