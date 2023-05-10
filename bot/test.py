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

#Download images
download.downloadImages(outputFileName)
#sign images
commands.wait(20)

imageEdit.addSignatures(outputFileName)
#add quote captions
#quotesAdded = imageEdit.addQuotes()
#add AI watermark
commands.wait(20)

waterMarksAdded = imageEdit.addWaterMarks(outputFileName)


commands.wait(5)
#Post images
print("Finished -> Send Tweets")
twitter.sendTweets(outputFileName)
#postingContent.postOutputImages(outputFileName)

print("Pushing updated output log to github")
gitPush.git_push("Update News Output log: " + str(date.today()))
