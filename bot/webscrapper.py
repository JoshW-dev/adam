import requests
import action
import random
from bs4 import BeautifulSoup


def scrape(numHeadlines):
    #BBC  news: world news headlines
    url = "https://www.bbc.com/news/world"
    print("Webscrapping...")
    print(url)
    print("# headlines = " +str(numHeadlines))
    #get headlines
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    stories = soup.findAll('h3',{'class':'gs-c-promo-heading__title'})
    print("# stories = "+ str(len(stories)))
    headlines = []
    for story in stories:
        headlines.append(story.text)
    #remove duplicates
    headlines = list(set(headlines))
    prompts =""
    #write to input text file
    i = 0
    for headline in headlines:
        print(headline)
        prompts+= headline + "\n"
        i+=1
        if(i>=numHeadlines):
            break
    action.writeToInput(prompts)
    print("Webscrapper complete")

def getQuotes(keywords):
    url = "https://www.brainyquote.com/search_results?q=" 
    print("Fetching Quotes" + str(keywords))
    
    for keyword in keywords:
        url+=keyword+"+"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    groups = soup.findAll('div',{'class':'bqQt'})
    quotes = []
    for group in groups:
        quote = (group.text.split("\n"))
        filteredQuote = [string for string in quote if string != ""]
        if (len(filteredQuote[0])<130):
            quotes.append(filteredQuote)

    #only return 1 random quote for now
    try:
        choice = random.choice(quotes)
    except:
        choice = ["",""]

    return choice