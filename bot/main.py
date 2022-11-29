from click import prompt
from clickerTyper import commands
import action
import pyautogui
import action 
import random
import time
import keyboard
import win32api, win32con
import yake
import requests
import pyperclip
import os
import webscrapper
import download
import twitter
import re
from dotenv import load_dotenv
import webbrowser
import SendPrompts

#Set painting styles
tags = ", wide burshstrokes, painting, news"


#erase old txt files
action.eraseInput()
action.eraseOutput()
commands.wait(2)

#get prompts and populate input.txt
webscrapper.scrape()


#open browser and go to discord midjourney chat
midjourney_chat = os.getenv('Midjourneybot-Channel')
webbrowser.open(midjourney_chat)
commands.wait(10)
commands.alignLeft()

print("Sending prompts...")
complete = SendPrompts.send(tags)
print("Prompts complete: " + str(complete))
#Download images
#action.downloadImages()


#generate images
    #Gen caption
    #save JobIDs
    #Download image
#Post image

#repeat


