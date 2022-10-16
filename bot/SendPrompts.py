import action 
import random
import pyperclip
from clickerTyper import commands

with open('./Inputs/input.txt') as f:
    prompts = f.read().splitlines()

tags = " --ar 2:3"


print("Started...")
for prompt in prompts:
    fullPrompt = (prompt +tags)
    print(fullPrompt)
    #Stage 1
    action.sendPrompt(fullPrompt)
    print("init gen...")
    complete = action.waitForPrompt(1)
    #Stage 2
    action.upscale1("U"+str(random.randint(1, 4))+"-Button.png")#randomly upscale 1 of 4 variations
    print("init upscale...")
    complete = action.waitForPrompt(2)
    #Stage 3
    action.upscale1("Remaster-Button.png")
    print("init remaster...")
    complete = action.waitForPrompt(3)
    #Stage 4
    action.upscale1("U1-Button.png")
    print("remaster upscale...")
    complete = action.waitForPrompt(4)
    print("prompt complete")
    
    #Stage 5 - copy headline and Job URL
    action.copyWebUrl()
    print("Grabbing Image URL...")    
    jobID = pyperclip.paste().split("www.midjourney.com/app/jobs/")[1]
    out = prompt + "##" + jobID + "\n"
    action.writeToOutput(out)
    print("Saved to output.txt")
    

    
print("done")