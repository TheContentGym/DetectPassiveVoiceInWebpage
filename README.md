# Detect Passive Voice In a (tech-doc) Webpage
<<<<<<< Updated upstream
**What is passive voice:** A form or set of forms of a verb in which the subject undergoes the action of the verb (example: they were killed as opposed to the active form he killed them ). 

**Why avoid passive voice:** Passive sentences tend to be wordier and also more difficult to read than active sentences. Sometimes, they tend to obscure the do-er of the action too. For example: "Mr A did the work" gives the right subject and better information compared to a wordier "The work was done". 

**Prerequisites for using the script:** 
=======
What is passive voice: A form or set of forms of a verb in which the subject undergoes the action of the verb (example: they were killed as opposed to the active form he killed them ). 
Why avoid passive voice: Passive sentences tend to be wordier and also more difficult to read than active sentences.

Prerequisites: 
>>>>>>> Stashed changes
* You should have python installed, of course, and the following two:
  * beautifulsoup
  * Spacy


By specifying URL of a page in this script, you can detect if there are any instances of passive voice in that page.

To use the script:
1. Enter the **url** of the webpage you want to check in the following variable: 
 
 `url = 'https://thecontentgym.wordpress.com/2022/05/09/a-non-engineer-attending-a-marathon-5-full-days-python-training-with-experienced-programmers/'`
 
2. Replace `body` with the name of the HTML tag you want to check. The value of *body* checks the whole <body> tag of the specified web page. You can specify smaller elements, such as *P* or *Div* (with or without attribute values). And when you do so, replace soup.find with *soup.find_all*.   
  
  `bd = soup.find('body')`
  
3. Run the script.   
  

