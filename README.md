# DetectPassiveVoiceInWebpage
By specifying URL of a page in this script, you can detect if there are any instances of passive voice in that page.
To use:
# Enter the url you want to check in the following variable: 
url = 'https://thecontentgym.wordpress.com/2022/05/09/a-non-engineer-attending-a-marathon-5-full-days-python-training-with-experienced-programmers/'
# Replace body with the name of the HTML tag you want to check. The value of body checks the whole body of the specified web page.   
bd = soup.find_all('body')

