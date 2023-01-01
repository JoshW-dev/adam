from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
import os
load_dotenv()
imagePath = os.getenv('Local-Download-Location')
import textwrap
import download


def addText2(imageName, text, type):
    print("Adding: " + text)
    print("To: " + imageName)        
    print("Type: " + type)        
    caption = text
    img = Image.open(imagePath + imageName)
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype('impact.ttf', size=50)
    d.text((10, 400), caption, fill='white', font=font,
        stroke_width=2, stroke_fill='black')
    img.save(imagePath + imageName)
    print("Added text")

#modularize to more than just quotes
def addText(imageName, text, type):
    print("Adding: " + text + "\nTo: " + imageName + "\nType: " + type) 
    img = Image.open(imagePath + imageName)
    font = ImageFont.truetype('./Assets/Arial.ttf', 25) 
    maxChars = 70
    text = addNewlines(text,maxChars)
    width, height = img.size
    position = (width*.05, height*.85)
    # get a drawing context
    d = ImageDraw.Draw(img, "RGBA")

    #textbook
    left, top, right, bottom = d.textbbox(position, text, font=font)    
    d.rectangle((left-5, top-5, right+5, bottom+5), fill= (255, 255, 255, 50))
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
                        addText((jobID+".png"),caption, "bottom-small")
                except:
                        print("An exception occurred")


#loop through all output images and add quotes
def addSignature(backgroundImage):
    print("Adding sig to " + backgroundImage)
    img1 = Image.open(imagePath + backgroundImage)
    img2 = Image.open('./Assets/signatureTS.png')
    width, height = img1.size

    back_im = img1.copy()
    back_im.paste(img2, (int(width*0.8), int(height*0.88)), img2)
    back_im.save(imagePath + backgroundImage, quality=100)
    print("Signed")

def addSignatures():
    print("Adding signatures to all output images")
    images = download.parseOutput()
    for image in images:
                try:
                        prompt = image.split("##")[0]
                        jobID = image.split("##")[1].replace("/", "" )
                        caption = image.split("##")[2]
                        addSignature(jobID + ".png")
                except:
                        print("An exception occurred")
