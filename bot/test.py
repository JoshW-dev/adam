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


testimage = "e726fae9-3caa-4809-aadb-ecc710e66ba2.png"
text = "I saw her in a dream, Exiting the bookstore lobby, I saw her in a dream, Exiting the bookstore lobby"
type="bottom-med"
imageEdit.addText(testimage, text, type)
print(len(text))    