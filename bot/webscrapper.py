import requests
import action
import random
from bs4 import BeautifulSoup


def scrape(numHeadlines,inputFileName):
    #BBC  news: world news headlines
    print("News - BBC World")
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
        prompts+= headline + "||BBC News"+"\n"
        i+=1
        if(i>=numHeadlines):
            break
    action.writeToInput(prompts,inputFileName)
    print("Webscrapper complete")



def scrapeFox(numHeadlines,inputFileName, newsUrl):
    #Fox news: world news headlines
    print("News - Fox News World")
    url = newsUrl
    print("Webscrapping...")
    print(url)
    print("# headlines = " +str(numHeadlines))
    #get headlines
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    
    stories = soup.findAll('h2',{'class':'title'})
    print("# stories = "+ str(len(stories)))
    
    headlines = []
    for story in stories:
        headlines.append(story.text)
        print(story.text)

    prompts =""
    #write to input text file
    i = 0
    for headline in headlines:
        print(headline)
        prompts+= headline + "||Fox News"+"\n"
        i+=1
        if(i>=numHeadlines):
            break
    action.writeToInput(prompts,inputFileName)


    print("Webscrapper complete")

def scrapeCNN(numHeadlines,inputFileName, newsUrl):
    #Fox news: world news headlines
    print("News - CNN World")
    url = newsUrl
    print("Webscrapping...")
    print(url)
    print("# headlines = " +str(numHeadlines))
    #get headlines
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')    

    stories = soup.findAll('div',{'class':'container_lead-plus-headlines__headline'})
    print("# stories = "+ str(len(stories)))
    headlines = []
    for story in stories:
        headlines.append(story.text)
    prompts =""
    #write to input text file
    i = 0
    for headline in headlines:
        prompts+= headline.replace("\n", "" ).strip() + "||CNN"+"\n"
        i+=1
        if(i>=numHeadlines):
            break
    action.writeToInput(prompts,inputFileName)
    print("Webscrapper complete")

def scrapeAlarabiya(numHeadlines,inputFileName, newsUrl):
    #Fox news: world news headlines
    print("News - Al Arabiya")
    url = newsUrl
    print("Webscrapping...")
    print(url)
    print("# headlines = " +str(numHeadlines))
    #get headlines
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')    

    stories = soup.findAll('h2',{'class':'sectionHero_title'})
    print("# stories = "+ str(len(stories)))
    headlines = []
    for story in stories:
        headline = story.contents[0].replace("\n", "" ).strip()
        print(headline)
        headlines.append(headline)
    prompts =""
    #write to input text file
    i = 0
    for headline in headlines:
        prompts+= headline + "||Al Arabiya"+"\n"
        i+=1
        if(i>numHeadlines):
            break
    action.writeToInput(prompts,inputFileName)
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