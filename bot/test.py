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
import imageEdit

#Download images
download.downloadImages()
#sign images
imageEdit.addSignatures()
#add quote captions
#imageEdit.addQuotes()

print("Finished -> Send Tweets")
#Post images
twitter.sendTweets()
