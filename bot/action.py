import random
from clickerTyper import commands


# send prompt to midjourney commandline
def sendPrompt(prompt):
    promptLocation = [650,1055] #discord webapp in chrome aligned to left side of laptop screen
    #todo: figure out a better way to set this

    commands.moveto(1200+10*random.random(),1000*random.random(),1)
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


#choose a versio to upscale 
def upscale1(choice):
    promptLocations = {1: [615,715], 2: [730,715], 3:[615,775], 4:[730,775],
    "max": [615,600],"light": [615,660], "beta": [615,720], "remaster": [615,780], 
    "remaster1": [615,840], "remaster2": [730,840], "remaster#1": [615,900]
    } #discord webapp in chrome aligned to left side of laptop screen
    #in order of U1, U2, U3, U4
    #todo: figure out a better way to set this and control upscaling
    commands.moveto(1200+10*random.random(),1000*random.random(),1)
    commands.wait(0.5)
    #move to button for chosen upscale option 
    commands.moveto(promptLocations[choice][0],promptLocations[choice][1],1)
    commands.click()
 
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
