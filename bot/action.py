import random
import yake
import requests
import shutil
import os
import download
import re
from dotenv import load_dotenv
load_dotenv()

from clickerTyper import commands

# send prompt to midjourney commandline
def sendPrompt(prompt):
    commands.movetoRandom(1200,1000,0.5)
    commands.wait(0.2)
    #move to discord chat line
    promptLocation = commands.locateButton("Text-Input.png", .7)
    commands.movetoRandom(promptLocation[0],promptLocation[1],.5)
    commands.click()
    commands.typeCharacters("/imagine")
    commands.presskey("enter")
    commands.wait(0.1)
    commands.typeCharacters(prompt)
    commands.wait(0.1)
    commands.presskey("enter")

def waitForPrompt(stage):
    loading = True
    commands.wait(15)
    print("Loading: " + str(loading))
    while loading:
        print("Stage " + str(stage) + ": loading...")
        commands.wait(3)
        complete = commands.checkPromptComplete(stage)
        loading = not complete
    print("Stage " + str(stage) + " Complete")
    return True

#choose a version to upscale 
def upscale1(buttonChoice):
    commands.movetoRandom(1200,1000,0.5)
    buttonLocation = commands.locateButton(buttonChoice, .7)
    commands.movetoRandom(buttonLocation[0],buttonLocation[1],.5)
    commands.click()
    commands.movetoRandom(1200,1000,0.5)

#keyword extraction
language = "en"
deduplication_threshold = 0.9
deduplication_algo = 'seqm'
windowSize = 1 
def keywords(input, numOfKeywords,max_ngram_size):
    kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)   
    keywords = kw_extractor.extract_keywords(input)
    list =[]
    for kw in keywords:
        list.append(kw[0])
    return list

def replaceBannedWords(message):
    #cycle through dictionary of midjourney banned terms and replace with acceptable words
    BannedwordsKill = ["Crucifixion", "Car crash", "Crucified", "Kill", "Slaughter", "Decapitate", "Killing", "Vivisection", "Massacre", "Suicide"]
    BannedwordsGore =  ["Blood", "Bloodbath", "Bloody", "Flesh", "Bruises", "Corpse", "Cutting", "Infested", "Gruesome", "Infected", "Sadist", "Teratoma", "Tryphophobia", "Wound", "Cronenberg", "Khorne", "Cannibal", "Cannibalism", "Visceral", "Guts", "Bloodshot", "Gory", "Surgery", "Hemoglobin"]
    BannedwordsTaboo = ["Fascist", "Nazi", "Prophet Mohammed", "Slave", "Coon", "Honkey"]
    BannedwordsDrugs = ["Cocaine", "Heroin", "Meth", "Crack"]

    replaceWordKill="slain"
    replaceWordGore = "painful"
    replaceWordTaboo = "evil"
    replaceWordDrugs = "drugs"

    for word in BannedwordsKill:
        cleanMessage = re.sub('(?i)'+re.escape(word), lambda m: replaceWordKill, message)
        message = cleanMessage
    for word in BannedwordsGore:
        cleanMessage = re.sub('(?i)'+re.escape(word), lambda m: replaceWordGore, message)
        message = cleanMessage
    for word in BannedwordsTaboo:
        cleanMessage = re.sub('(?i)'+re.escape(word), lambda m: replaceWordTaboo, message)
        message = cleanMessage
    for word in BannedwordsDrugs:
        cleanMessage = re.sub('(?i)'+re.escape(word), lambda m: replaceWordDrugs, message)
        message = cleanMessage

    return message

def writeToInput(lines):
    f = open("./Inputs/input.txt", "w")
    f.write(lines)
    f.close()

def writeToOutput(lines):
    with open('./Outputs/output.txt','a') as f:
        f.write(lines)

def copyWebUrl():
    #find a better way to do this
    
    #saw some bugs where the copy url button was not recognized, if this happens more, look into better way
    commands.movetoRandom(1200,1000,0.5)
    buttonLocation = commands.locateButton("Web-Button.png", .7)
    commands.movetoRandom(buttonLocation[0],buttonLocation[1],.5)
    commands.rightClick()
    commands.wait(0.1)
    buttonLocation = commands.locateButton("Copy-Link-Button.png", .7)
    commands.movetoRandom(buttonLocation[0],buttonLocation[1],.5)
    commands.click()
    commands.movetoRandom(1200,1000,0.5)


#needs rework

def downloadImage(url, name):
    downloadLocation = os.getenv('Local-Download-Location')
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(downloadLocation + name+".png", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

def downloadImages():
    #download all generated images from output.txt
    images = download.parseOutput()
    download.downloadOutputs(images)    

#post on instagram
def postInsta(file, caption):  
    uploadLocation = [1645,160] #discord webapp in chrome aligned to left side of laptop screen  

    print("start insta post")
    commands.moveto(1000*random.random(),1000*random.random(),1)
    commands.wait(0.5)
    #move to upload button
    commands.moveto(uploadLocation[0],uploadLocation[1],1)
   
    #finish upload
    print(file)
    print(caption)
    print("end insta post")


#postInsta("file1","an insta post #tag1 #tag2")
