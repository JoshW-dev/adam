from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
import os
load_dotenv()
imagePath = os.getenv('Local-Download-Location')
import textwrap
import download

#modularize to more than just quotes
def addText(imageName, text, type):
    print("Adding: " + text)
    print("To: " + imageName)        

    maxCharactersPerLine = 50
    text = addNewlines(text,maxCharactersPerLine)
    FONT_PATH = './Assets/roboto/Roboto-Medium.ttf'
    font_size = 80
    font = ImageFont.truetype(FONT_PATH, size=font_size)
    
    # Open an Image
    img = Image.open(imagePath + imageName)
    
    width, height = img.size
    position = (width*.1, height*.8)
    # get a drawing context
    d = ImageDraw.Draw(img, "RGBA")
    #textbook
    bbox = d.textbbox(position, text, font=font)    
    d.rectangle(bbox, fill= (0, 0, 0, 110))
    # draw multiline text
    d.multiline_text(position, text, font = font, fill=(255, 255, 255))
    img.save(imagePath + imageName)
    print("Added text")

#loop through all output images and add tied quotes
def addQuotes():
    print("Adding quotes to all output images...")
    images = download.parseOutput()
    for image in images:
                try:
                        prompt = image.split("##")[0]
                        jobID = image.split("##")[1].replace("/", "" )
                        caption = image.split("##")[2]                        
                        addText((jobID+".png"),caption, "nullType")
                except:
                        print("An exception occurred")
    

def addNewlines(text,maxChars):
    #print(text)
    s = ('\n'.join(textwrap.wrap(text, maxChars)))
    return s.replace("-", "\n     -" )

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
    