import action

urlPrefix = "https://mj-gallery.com/"
urlSuffix = "/grid_0.png"
with open('./Outputs/output.txt') as f:
        lines = f.read().splitlines()

for line in lines:
        prompt = line.split("##")[0]
        jobID = line.split("##")[1].replace("/", "" )
        print(prompt)
        print(jobID)
        url = urlPrefix + jobID + urlSuffix
        action.downloadImage(url, jobID)
