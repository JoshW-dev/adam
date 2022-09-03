import random
from clickerTyper import commands


# send prompt to midjourney commandline
def sendPrompt(prompt):
    promptLocation = [650,1055] #discord webapp in chrome aligned to left side of laptop screen
    #todo: figure out a better way to set this

    print("start prompt")
    commands.moveto(1000*random.random(),1000*random.random(),1)
    commands.wait(0.5)
    #move to discord chat line
    commands.moveto(promptLocation[0],promptLocation[1],1)
    #move to discord chat line
    commands.click()
    commands.typeCharacters("/imagine")
    commands.presskey("enter")
    commands.wait(0.1)
    commands.typeCharacters(prompt)
    commands.wait(0.1)
    commands.presskey("enter")
    print("end prompt")

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



postInsta("file1","an insta post #tag1 #tag2")
# sendPrompt("a happy duck")