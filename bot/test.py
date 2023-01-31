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
imageEdit.addSignatures(outputFileName)
waterMarksAdded = imageEdit.addWaterMarks(outputFileName)
commands.wait(5)
print("Finished -> Send Tweets")
twitter.sendTweets(outputFileName)
postingContent.postOutputImages(outputFileName)
