from PIL import Image
from PIL import ImageDraw
from dotenv import load_dotenv
import os
load_dotenv()
imagePath = os.getenv('Local-Download-Location')



def addText(imageName, text):
    print("Adding: " + text)
    print("To: " + imageName)        
    # Open an Image
    img = Image.open(imagePath + imageName)
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
    # Add Text to an image
    I1.text((28, 36), text, fill=(255, 0, 0))
    # Display edited image
    img.show()    
    # Save the edited image
    img.save(imagePath + imageName)