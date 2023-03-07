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

inputFileName="input.txt"
outputFileName="output.txt"

tags = ", news, dslr, award winning photography,"


webscrapper.scrapeAlarabiya(3,inputFileName,"https://english.alarabiya.net/News/world")
