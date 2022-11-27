from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
import os
load_dotenv()
imagePath = os.getenv('Local-Download-Location')



def addText(imageName, text, type):
    print("Adding: " + text)
    print("To: " + imageName)        
    

    maxCharactersPerLine = 30

    FONT_PATH = './Assets/roboto/Roboto-Light.ttf'
    font_size = 100
    font = ImageFont.truetype(FONT_PATH, size=font_size)
    # Open an Image
    img = Image.open(imagePath + imageName)
    
    width, height = img.size
    print(width)
    print(height)

    # get a drawing context
    d = ImageDraw.Draw(img)

    # draw multiline text
    d.multiline_text((width*.2, height*.8), text, font = font, fill=(255, 255, 255))

    img.save(imagePath + imageName)

