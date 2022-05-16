# DetectPassiveVoiceInWebpage
Prerequisites: 
* You should have python installed, of course, and the following two:
  * beautifulsoup
  * Spacy


By specifying URL of a page in this script, you can detect if there are any instances of passive voice in that page.
To use:
1. Enter the **url** of the webpage you want to check in the following variable: 
 
 `url = 'https://thecontentgym.wordpress.com/2022/05/09/a-non-engineer-attending-a-marathon-5-full-days-python-training-with-experienced-programmers/'`
 
2. Replace `body` with the name of the HTML tag you want to check. The value of body checks the whole body of the specified web page.   
  
  `bd = soup.find_all('body')`
  
3. Run the script.   
  

