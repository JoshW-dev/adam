from ast import keyword
import action 
import random
import pyperclip
import webscrapper

from clickerTyper import commands


def send(tags):
    with open('./Inputs/input.txt') as f:
        prompts = f.read().splitlines()

    print("Started...")
    for prompt in prompts:
        keywords = ", " + ', '.join(action.keywords(prompt,2,2))
        fullPrompt = (prompt +keywords+ tags)
        print(fullPrompt)
        #Stage 1
        action.sendPrompt(fullPrompt)
        #regen keywords for quote gen
        keywords = action.keywords(prompt,3,1)
        #Get quote 
        quoteList = webscrapper.getQuotes(keywords)
        quote = "\""+quoteList[0] +"\"" +"\n\n-"+ quoteList[1]
        print(quote)
        print("init gen...")
        commands.wait(5)
        if (commands.checkBanned()):
            continue
        print("not banned")
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
        out = prompt + "\n##" + jobID + "## \n\n" + quote+  "\n\n ------\n\n\n"
        action.writeToOutput(out)
        print("Saved to output.txt")
        
    print("done")
    return True
        
    