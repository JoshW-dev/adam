import os
import time
import random
from keyboard import wait
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
        
    def rightClick():
        pyautogui.click(button='right')
    
    def typeCharacters(string):
        pyautogui.write(string, interval=0.05)

    def presskey(keyName):
        pyautogui.press(keyName)

    def hotkey():
        pyautogui.hotkey('alt', 'tab') 
    def alignLeft():
        pyautogui.hotkey('win', 'left') 

    def wait(sleeptime):
        time.sleep(sleeptime)
    
    def cursorLocation():
        return pyautogui.position()

    def pixelColor(location):
        return pyautogui.pixel(location[0], location[1])
        

    def locateButton(buttonName, alpha):
        buttonPoint = pyautogui.locateCenterOnScreen('./Assets/'+buttonName, confidence=alpha, region=(475,540,460,650)) #region is bottom left area of screen with output images+buttons
        print("Button point: " + str(buttonPoint))
        #Will return "None" if not found (must convert to str)
        #this method is kinda buggy and relies text scaling (works best at %150)
        attemps = 0
        while(str(buttonPoint) =="None" and attemps <5):
            buttonPoint = pyautogui.locateCenterOnScreen('./Assets/'+buttonName, confidence=(alpha), region=(475,540,460,650)) #region is bottom left area of screen with output images+buttons
            attemps+=1
            commands.wait(0.2)
        return buttonPoint

    def checkPromptComplete(stage):
        #ensure cursor is not hovering over buttons when checking
        #stage 1: check complete after initial gen - check that U1 and V1 buttons show
        if stage == 1 or stage == 3:
            U1ButtonLocation = commands.locateButton("U1-Button.png", 0.7)
            if (str(U1ButtonLocation) == 'None'):
                return False
            else:
                return True
        #stage 2: check complete after first upscaling - check that remaster and variation buttons show
        elif stage == 2:
            remasterButtonLocation = commands.locateButton("Remaster-Button.png", 0.7)
            if (str(remasterButtonLocation) == 'None'):
                return False
            else:
                return True
        #stage 4: check complete after second upscaling - check that remaster and variation buttons show
        elif stage == 4:
            Variations_Web_Location = commands.locateButton("Variations&Web-Button.png", 0.7)
            if (str(Variations_Web_Location) == "None"):
                return False
            else:
                return True
        
    def checkBanned():
        buttonPoint = pyautogui.locateCenterOnScreen('./Assets/'+"banned.png", confidence=.9, region=(475,540,460,650)) #region is bottom left area of screen with output images+buttons
        if (str(buttonPoint) =="None" ):
            return False
        return True