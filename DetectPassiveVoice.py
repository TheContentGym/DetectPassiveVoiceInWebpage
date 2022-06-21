from bs4 import BeautifulSoup
import requests
import lxml
import spacy
nlp = spacy.load("en_core_web_sm")
#1) Send a get query to the website and receive HTML
url = 'https://docs.up42.com/data'
response = requests.get(url)
#2) Parse the HTML
soup = BeautifulSoup(response.text,'lxml')
#3) Extracting the data we actually want.
bd = soup.find('body')
#4) Check the data in the variable for passive voice using the SpaCy library
doc = nlp(bd.text)
for token in doc:
    if (token.dep_ == "nsubjpass"):
#5) Print the results        
        print("passive voice found. Nominal subject:",token.text,token.lemma_, token.pos_, token.tag_, token.dep_)
    elif (token.dep_ == "auxpass"):
        print("passive voice found in nominal subject:",token.text,token.lemma_, token.pos_, token.tag_, token.dep_)

    else:
        print('passive voice not detected')
        break 
