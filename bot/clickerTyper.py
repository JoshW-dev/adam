import os
import time
import random
import pyautogui


class commands:
    def moveto(xcord, ycord, dur):
        pyautogui.moveTo(xcord, ycord, duration=dur, tween=pyautogui.easeInOutQuad)

    def movetoRandom(xcord, ycord, dur):
        #add some randomness to desired location to mimic human action
        ran = random.randint(-3,3)
        pyautogui.moveTo(xcord+ran, ycord+ran, duration=dur, tween=pyautogui.easeInOutQuad)
            
    def click():
        pyautogui.click()

    def typeCharacters(string):
        pyautogui.write(string, interval=0.1)

    def presskey(keyName):
        pyautogui.press(keyName)

    def hotkey():
        pyautogui.hotkey('alt', 'tab') 

    def wait(sleeptime):
        time.sleep(sleeptime)
    
    def cursorLocation():
        return pyautogui.position()

    def pixelColor(location):
        return pyautogui.pixel(location[0], location[1])
        

    def checkPromptComplete():
        #ensure cursor is not hovering over buttons when checking
        buttonLocationGrey = (636, 971)
        buttonLocationWhite = (632, 961)
        buttonGrey = (79, 84, 92)
        buttonWhite = (255, 255, 255)
        #check that V3 button appears in correct area
        # Todo: find a better way to do this        
        if (commands.pixelColor(buttonLocationGrey) == buttonGrey and 
            commands.pixelColor(buttonLocationWhite) == buttonWhite):
            print("Prompt Complete")
            return True    
        return False

    def locateButton(buttonName, alpha):
        location = pyautogui.locateOnScreen('./Assets/'+buttonName, confidence=alpha)
        buttonPoint = pyautogui.center(location)
        return buttonPoint