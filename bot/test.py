from clickerTyper import commands
import action
import pyautogui
import action 
import random
import time
import keyboard
import win32api, win32con



location = pyautogui.locateOnScreen('Assets\U1-Button.png')
print(location)

wait(100)

complete = False    
while not complete:
    complete = commands.checkPromptComplete()
    time.sleep(1)
    print("...")
print("done")