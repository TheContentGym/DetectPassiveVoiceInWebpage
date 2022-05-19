from bs4 import BeautifulSoup
import requests
import lxml
import spacy
nlp = spacy.load("en_core_web_sm")

url = 'https://thecontentgym.wordpress.com/2022/05/09/a-non-engineer-attending-a-marathon-5-full-days-python-training-with-experienced-programmers/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
bd = soup.find('body')

doc = nlp(bd.text)
for token in doc:
    if (token.dep_ == "nsubjpass"):
        print("passive voice found. Nominal subject:",token.text)
    elif (token.dep_ == "auxpass"):
        print("passive voice found in nominal subject:",token.text)

