import requests
import action
from bs4 import BeautifulSoup
#BBC  news: world news headlines
url = "https://www.bbc.com/news/world"

#get headlines
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stories = soup.findAll('h3',{'class':'gs-c-promo-heading__title'})
headlines = []
for story in stories:
    headlines.append(story.text)
#remove duplicates
headlines = list(set(headlines))

prompts =""

#write to input text file
for headline in headlines:
    prompts+= headline + "\n"
action.writeToInput(prompts)
