import requests
import action
import random
from bs4 import BeautifulSoup


def scrape():
    #BBC  news: world news headlines
    url = "https://www.bbc.com/news/world"
    print("Webscrapping...")
    print(url)

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
    print("Webscrapper complete")
    print(str(len(headlines)) + " new prompts")

def getQuotes(keywords):
    url = "https://www.brainyquote.com/search_results?q=" 
    print("Fetching Quotes")
    
    for keyword in keywords:
        url+=keyword+"+"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    groups = soup.findAll('div',{'class':'bqQt'})
    quotes = []
    for group in groups:
        quote = (group.text.split("\n"))
        filteredQuote = [string for string in quote if string != ""]
        quotes.append(filteredQuote)

    #only return 1 random quote for now
    return random.choice(quotes)
