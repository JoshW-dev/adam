from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
import os
load_dotenv()
imagePath = os.getenv('Local-Download-Location')
import textwrap
import download

#modularize to more than just quotes
def addText(imageName, text, type):
    print("Adding: " + text + "\nTo: " + imageName + "\nType: " + type) 
    img = Image.open(imagePath + imageName)
    width, height = img.size
    
    if type == "bottom-small":
        fontSize = 25
        maxChars = 70
        position = (width*.05, height*.85)
    elif type == "bottom-med":
        fontSize = 35
        maxChars = 54
        position = (width*.05, height*.83)
    elif type == "water-mark":
        fontSize = 30
        maxChars = 100
        position = (width*.1, height*.93)
    
    elif type == "topLeft-small":
        fontSize = 20
        maxChars = 70
        position = (width*0.005, height*0.005)
    else:
        fontSize = 40
        maxChars = 48
        position = (width*.1, height*.75)
    
    font = ImageFont.truetype('./Assets/Arial.ttf', fontSize) 
    text = addNewlines(text,maxChars)
    # get a drawing context
    d = ImageDraw.Draw(img, "RGBA")

    #textbook
    left, top, right, bottom = d.textbbox(position, text, font=font)    
    d.rectangle((left-5, top-5, right+5, bottom+5), fill= (255, 255, 255, 75))
    d.text(position, text, font=font, fill="black")

    # draw multiline text
    d.multiline_text(position, text, font = font, fill=(0, 0, 0))
    img.save(imagePath + imageName)
    print("Added text")

def addNewlines(text,maxChars):
    t = ('\n'.join(textwrap.wrap(text, maxChars)))
    return t

#loop through all output images and add tied quotes
def addQuotes():
    print("Adding quotes to all output images...")
    images = download.parseOutput()
    for image in images:
                try:
                        prompt = image.split("##")[0]
                        jobID = image.split("##")[1].replace("/", "" )
                        caption = image.split("##")[2]                        
                        addText((jobID+".png"),caption, "bottom-med")
                except:
                        print("An exception occurred")
                        return (True)
def addWaterMarks(outputFileName):
    print("Adding Watermark to all output images...")
    images = download.parseOutput(outputFileName)
    for image in images:
                try:
                        prompt = image.split("##")[0]
                        jobID = image.split("##")[1].replace("/", "" )
                        caption = "AI GENERATED @ai_adam_"
                        addText((jobID+".png"),caption, "water-mark")
                except:
                        print("An exception occurred")
                        return (True)

#loop through all output images and add quotes
def addSignature(backgroundImage):
    print("Adding sig to " + backgroundImage)
    img1 = Image.open(imagePath + backgroundImage)
    img2 = Image.open('./Assets/signatureTS.png')
    width, height = img1.size

    back_im = img1.copy()
    back_im.paste(img2, (int(width*0.8), int(height*0.89)), img2)
    back_im.save(imagePath + backgroundImage, quality=100)
    print("Signed")

def addSignatures(outputFileName):
    print("Adding signatures to all output images")
    images = download.parseOutput(outputFileName)
    for image in images:
                try:
                        prompt = image.split("##")[0]
                        jobID = image.split("##")[1].replace("/", "" )
                        caption = image.split("##")[2]
                        addSignature(jobID + ".png")
                except:
                        print("An exception occurred")
def cleanFolder():
    print("deleting all saved generated images")
    dir_name = "./GeneratedImages"
    test = os.listdir(dir_name)
    for item in test:
        if item.endswith(".png"):
            os.remove(os.path.join(dir_name, item))