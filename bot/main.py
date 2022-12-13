from click import prompt
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

#Set painting styles
tags = ", wide brushstrokes, painting, news, realistic, award winning photography"

start = time.time()


#erase old txt files
action.eraseInput()
action.eraseOutput()
commands.wait(2)

#get prompts and populate input.txt
webscrapper.scrape(10)

#open browser and go to discord midjourney chat
midjourney_chat = os.getenv('Midjourneybot-Channel')
webbrowser.open(midjourney_chat)
commands.wait(10)
commands.alignLeft()

print("Sending prompts...")
complete = SendPrompts.send(tags)
print("Main - Prompts complete: " + str(complete))

#Download images
download.downloadImages()
#sign images
imageEdit.addSignatures()


#add quote captions
#imageEdit.addQuotes()

print("Finished -> Send Tweets")
#Post images
twitter.sendTweets()
#repeat
print("Complete")
end = time.time()

executionLength = end - start
print("Total execution time: " + executionLength)
