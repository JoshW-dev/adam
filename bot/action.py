import random
from clickerTyper import commands


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
    


def writeToInput(lines):
    f = open("./Inputs/input.txt", "w")
    f.write(lines)
    f.close()


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
