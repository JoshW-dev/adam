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
import gitPush
from datetime import date

inputFileName="input.txt"
outputFileName="output.txt"

tags = ", news, dslr, award winning photography,"



print("Pushing updated output log to github")
gitPush.git_push("Update News Output log: " + str(date.today()))