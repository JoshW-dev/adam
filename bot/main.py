from clickerTyper import commands
import action
import os
import webscrapper
import download
import twitter
import webbrowser
import SendPrompts
import imageEdit
import time
import postingContent
#Set painting styles
tags = ", news, realistic, award winning photography, creative, rich colors, photograph,"
inputFileName="input.txt"
outputFileName="output.txt"

start = time.time()

#clear commandline
for i in range(50):
    print()
print("Adam: Starting Webscrape")
print("News - BBC World")
for i in range(5):
    commands.wait(1)
    print(str(i)+"...")
print("rewriting")
#erase old txt files
action.eraseInput(inputFileName)
action.eraseOutput(outputFileName)

commands.wait(1)

#get prompts and populate input file
webscrapper.scrape(8,inputFileName)
commands.wait(3)

#open browser and go to discord midjourney chat
midjourney_chat = os.getenv('Midjourneybot-Channel')
webbrowser.open(midjourney_chat)
commands.wait(10)
commands.alignLeft()

print("Sending prompts...")
complete = SendPrompts.send(tags,inputFileName,outputFileName)
print("Main - Prompts complete: " + str(complete))

#Download images
download.downloadImages()
#sign images
imageEdit.addSignatures()
#add quote captions
#quotesAdded = imageEdit.addQuotes()
#add AI watermark
waterMarksAdded = imageEdit.addWaterMarks()


commands.wait(5)
#Post images
print("Finished -> Send Tweets")
twitter.sendTweets()
postingContent.postOutputImages()

#sending complete 
print("Complete")
end = time.time()

executionLength = end - start
print("Total execution time: " + str(executionLength/60) + " minutes")
