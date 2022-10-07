from clickerTyper import commands
import action
import pyautogui
import action 
import random
import time
import keyboard
import win32api, win32con


action.sendPrompt("Still life painting --ar 2:3")
    
commands.wait(10)
complete = False
while not complete:
    complete = commands.checkPromptComplete()
    print("Loading...")
    commands.wait(1)

