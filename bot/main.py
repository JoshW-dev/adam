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
import gitPush
from datetime import date

#Set painting styles
tags = ", abstract painting"
#tags = " --v 5"

inputFileName="input.txt"
outputFileName="output.txt"

start = time.time()

#clear commandline
for i in range(50):
    print()
print("Adam: Starting Webscrape")
for i in range(5):
    commands.wait(1)
    print(str(i)+"...")
print("rewriting")
#erase old txt files
action.eraseInput(inputFileName)
action.eraseOutput(outputFileName)

commands.wait(1)


#get prompts and populate input file

#BBC
webscrapper.scrape(3,inputFileName)
webscrapper.scrapeFox(3,inputFileName,"https://www.foxnews.com/world")
webscrapper.scrapeCNN(3,inputFileName,"https://www.cnn.com/world")
webscrapper.scrapeAlarabiya(3,inputFileName,"https://english.alarabiya.net/News/world")

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
download.downloadImages(outputFileName)
#sign images
imageEdit.addSignatures(outputFileName)
#add quote captions
#quotesAdded = imageEdit.addQuotes()
#add AI watermark
waterMarksAdded = imageEdit.addWaterMarks(outputFileName)


commands.wait(5)
#Post images
print("Finished -> Send Tweets")
twitter.sendTweets(outputFileName)
#postingContent.postOutputImages(outputFileName)

#sending complete 
print("Complete")
end = time.time()

executionLength = end - start
print("Total execution time: " + str(executionLength/60) + " minutes")

print("Pushing updated output log to github")
gitPush.git_push("Update News Output log: " + str(date.today()))