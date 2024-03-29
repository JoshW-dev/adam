from ast import keyword
import action 
import random
import pyperclip
import webscrapper

from clickerTyper import commands

def send(tags,inputFileName,outputFileName):
    with open('./Inputs/'+inputFileName) as f:
        prompts = f.read().splitlines()
        
    print("Started...")
    for prompt in prompts:
        hashTags = " #News #AI #Art #GPT"

        headline = prompt.split("||")[0]
        source=prompt.split("||")[1]
        hashTags = hashTags+" #"+source.replace(" ","")
        print(hashTags)
        prompt = action.replaceBannedWords(headline)
        keywords = ", " + ', '.join(action.keywords(prompt,2,2))
        fullPrompt   = (prompt +keywords+ tags)
        print(fullPrompt)
        #Stage 1
        action.sendPrompt(fullPrompt)
        #regen keywords for quote gen
        #keywords = action.keywords(prompt,3,1)
        
        #Get quote 
        #quoteList = webscrapper.getQuotes(keywords)
        #quote = "\""+quoteList[0] +"\"" +"\n    -"+ quoteList[1]
        
        #create caption
        keywordTags = ""
        keywords = action.keywords(headline,3,1)
        for i in range(len(keywords)):
            keywordTags += " #"+keywords[i].capitalize()
            
        caption = headline + "\n-"+source+"\n\n" +keywordTags+ hashTags
        print(caption)
        print("init gen...")
        commands.wait(5)
        if (commands.checkBanned()):
            continue
        print("not banned")
        commands.wait(15)

        
        '''
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
 
        '''
 
        #todo: come up with a solution to get te job ID
        jobID= "..."
        out = headline + "\n##" + jobID + "##\n" + caption+  "\n ------\n"
        action.writeToOutput(out,outputFileName)
        print("Saved to "+outputFileName)
        
    print("done")
    return True
        
    