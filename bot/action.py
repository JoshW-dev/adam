import random
import yake
from clickerTyper import commands

#keyword extraction
language = "en"
max_ngram_size = 2
deduplication_threshold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 2
kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)   

# send prompt to midjourney commandline
def sendPrompt(prompt):
    commands.movetoRandom(1200,1000,0.5)
    commands.wait(0.2)
    #move to discord chat line
    promptLocation = commands.locateButton("Text-Input.png", .9)
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
    buttonLocation = commands.locateButton(buttonChoice, .9)
    commands.movetoRandom(buttonLocation[0],buttonLocation[1],.5)
    commands.click()
    commands.movetoRandom(1200,1000,0.5)
    
def keywords(input):
    keywords = kw_extractor.extract_keywords(input)
    list =""
    for kw in keywords:
        list+= ", "+ kw[0]
    return list


def writeToInput(lines):
    f = open("./Inputs/input.txt", "w")
    f.write(lines)
    f.close()


def copyWebUrl():
    #find a better way to do this
    
    #saw some bugs where the copy url button was not recognized, if this happens more, look into better way
    commands.movetoRandom(1200,1000,0.5)
    buttonLocation = commands.locateButton("Web-Button.png", .9)
    commands.movetoRandom(buttonLocation[0],buttonLocation[1],.5)
    commands.rightClick()
    buttonLocation = commands.locateButton("Copy-Link-Button.png", .7)
    commands.movetoRandom(buttonLocation[0],buttonLocation[1],.5)
    commands.click()
    commands.movetoRandom(1200,1000,0.5)


#needs rework

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
