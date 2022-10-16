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
import download 



urlPrefix = "https://mj-gallery.com/"
urlSuffix = "/grid_0.png"
with open('./Outputs/output.txt') as f:
        lines = f.read().splitlines()

for line in lines:
        prompt = line.split("##")[0]
        jobID = line.split("##")[1].replace("/", "" )
        print(prompt)
        print(jobID)
        url = urlPrefix + jobID + urlSuffix
        action.downloadImage(url, jobID)



'''

downloadLocation = "C:/Users/Josh Wade/Desktop/code/Projects/adam/bot/GeneratedImages/"
imageName = "test.png"
url = "https://mj-gallery.com/5a2d5264-a627-4492-8905-b353287e84b9/grid_0.png"

action.downloadImage(downloadLocation, url, imageName)


with open('./Outputs/output.txt') as f:
        lines = f.read().splitlines()

for line in lines:
        prompt = line.split(",")[0]
        jobID = line.split("www.midjourney.com/app/jobs/")[1]
        print(jobID)
url = "https://mj-gallery.com/5a2d5264-a627-4492-8905-b353287e84b9/grid_0.png"
action.downloadImage(url)
'''

