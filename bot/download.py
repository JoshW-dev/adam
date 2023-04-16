import action
import os
def parseOutput(outputFileName):
        with open('./Outputs/'+outputFileName) as f:
                images = f.read().split("------") 
                return images
        #pass returned image list to downloadOutputs()
def downloadImage(prompt, jobID, caption):
        urlPrefix = "https://cdn.midjourney.com/"
        #urlSuffix = "/0_0.png"

        urlSuffix = "/grid_0.png"

        #need to investigate and improve how this is working, currently picking first U1 option everytime.
        #I think midjourney's database naming system changed recently (04-14)
        url = urlPrefix + jobID + urlSuffix
        action.downloadImage(url, jobID)


def downloadOutputs(images):
        #images input is array of strings with prompt, ID & quote/caption
        for image in images:
                try:
                        prompt = image.split("##")[0]
                        jobID = image.split("##")[1].replace("/", "" )
                        caption = image.split("##")[2]
                        downloadImage(prompt, jobID, caption)
                except:
                        print("An exception occurred")    
    
def downloadImages(outputFileName):
    #download all generated images from output file
    images = parseOutput(outputFileName)
    downloadOutputs(images)    
