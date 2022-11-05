import action

def parseOutput():
        with open('./Outputs/output.txt') as f:
                images = f.read().split("------") 
                return images
        #pass returned image list to downloadOutputs()
def downloadImage(prompt, jobID, caption):
        urlPrefix = "https://mj-gallery.com/"
        urlSuffix = "/grid_0.png"
        url = urlPrefix + jobID + urlSuffix
        print("Downloading Image: " + jobID)
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
    