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

#Download images
download.downloadImages(outputFileName)
#sign images
imageEdit.addSignatures(outputFileName)
#add quote captions
#quotesAdded = imageEdit.addQuotes()
#add AI watermark
waterMarksAdded = imageEdit.addWaterMarks(outputFileName)


commands.wait(5)
#Post images
print("Finished -> Send Tweets")
twitter.sendTweets(outputFileName)
postingContent.postOutputImages(outputFileName)

#sending complete 
print("Complete")