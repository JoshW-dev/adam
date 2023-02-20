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
outputFileName="output.txt"

prompt="Victim's relative lunges at gunman before sentence"
keywordTags = ""
keywords = action.keywords(prompt,2,1)
for i in range(len(keywords)):
    keywordTags += " #"+keywords[i]
print(keywordTags)