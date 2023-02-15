from click import prompt
from clickerTyper import commands
import action
import pyautogui
import action 
import random
import time
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
import imageEdit
import postingContent as postInsta
import postingContent


midjourney_chat = os.getenv('Midjourneybot-Channel')
webbrowser.open(midjourney_chat)
commands.wait(10)
commands.alignLeft()

print("Sending prompts...")
tags=", cartoon, tim warnes"
inputFile="input-test.txt"
outputFile="output-test.txt"

complete = SendPrompts.send(tags,inputFile,outputFile)
#Download images
download.downloadImages(outputFile)
