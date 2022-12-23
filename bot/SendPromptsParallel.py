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
    numPrompts = len(prompts)
    for prompt in prompts:
        headline = prompt
        prompt = action.replaceBannedWords(headline)
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
        #print(quote)
        
        print("init gen...")
    print("all prompts sent")
    upscaling = True #bool for keeping track to see how many prompts still need upscaling
    Ids = [] #array for collecting generated image IDs and avoiding double recordings
    while():    
        '''
        every second
            check to see if upscale buttons found
                if found click random U1-U4
            check to see if Web button is found
                if found copy weburl and check against IDs[]
                    if new, add and add to output
        '''
        #look for upscale button cluser - once clicked, one should turn blue and is no longer found
        upscaleButton = commands.locateButton("U1-Button.png", .7)


        #if nothing found
        print("Waiting...")
        complete = action.waitForPrompt(1)
        #Stage 2
        action.upscale1("U"+str(random.randint(1, 4))+"-Button.png")#randomly upscale 1 of 4 variations
        print("init upscale...")
        
        complete = action.waitForPrompt(4)
        print("prompt complete")
        
        #Stage 5 - copy headline and Job URL
        action.copyWebUrl()
        print("Grabbing Image URL...")
        jobID = pyperclip.paste().split("www.midjourney.com/app/jobs/")[1]
        out = headline + "\n##" + jobID + "## \n\n" + quote+  "\n\n ------\n\n\n"
        action.writeToOutput(out)
        print("Saved to output.txt")
        
    print("done")
    return True
        
    