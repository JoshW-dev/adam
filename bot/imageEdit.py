from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
import os
load_dotenv()
imagePath = os.getenv('Local-Download-Location')
import textwrap


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
    

def addQuotes():
    print("Adding quotes to output images")
    #loop
    image = "7f0532b6-7b00-464c-95df-bb494ab1032c.png"
    imageEdit.addText(image, '\"The future belongs to those who believe in the beauty of their dreams.\" \n -Eleanor Roosevelt', 'null')
