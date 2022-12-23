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
import postingContent as postInsta


hastags="#News #AI #Art #BBC"
#test auto post image
testUrl= 'https://cdn.midjourney.com/73e37430-ca21-42e1-a8d3-695ce775487e/grid_0.png'
testCaption = 'This is a Test \n\n' + hastags
postInsta.postImage(testUrl,testCaption)