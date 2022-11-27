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


#erase old input file
action.eraseInput()
commands.wait(1)

#get prompts and populate input.txt
webscrapper.scrape()


#open browser and go to discord midjourney chat
midjourney_chat = os.getenv('Midjourneybot-Channel')
webbrowser.open(midjourney_chat)
commands.wait(10)
commands.alignLeft()

print("Sending prompts...")
SendPrompts.send(tags)

#Download images
#action.downloadImages()


#generate images
    #Gen caption
    #save JobIDs
    #Download image
#Post image

#repeat


