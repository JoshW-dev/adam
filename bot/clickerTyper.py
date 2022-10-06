import os
import time
import pyautogui


class commands:
    def moveto(xcord, ycord, dur):
        pyautogui.moveTo(xcord, ycord, duration=dur, tween=pyautogui.easeInOutQuad)
            
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
    
    def checkPromptComplete():
        #ensure cursor is not hovering over buttons when checking
        buttonLocation = (636, 971)
        buttonGrey = (79, 84, 92)
        currentColor = pyautogui.pixel(buttonLocation[0], buttonLocation[1])
        if currentColor == buttonGrey:
            print("Prompt Complete")
            return True    
        return False

    def locateButton(button):
        if button == "U!":
            location = pyautogui.locateOnScreen('Assets\U1-Button.png')
        return location