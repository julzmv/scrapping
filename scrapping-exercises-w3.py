import requests
from bs4 import BeautifulSoup
from lxml import etree
from lxml import html
from urllib.request import urlopen

url = "https://en.wikipedia.org/wiki/Michael_Schumacher" # uniform resource locator 

response = urlopen(url)

# soup = BeautifulSoup(response.text, features="html.parser")

# content = soup.get_text()

#print(content)
#xpath = '//*[@id="bodyContent"]'

xpath = '//*[@id="mw-content-text"]' 

#xpath = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[6]'

#htmlparser = etree.HTMLParser()
#tree = etree.parse(response, htmlparser)
#node = tree.xpath(xpath)[0]
#for child in node:
    #print(child.text)

root = html.parse(response).getroot()
element = root.get_element_by_id("mw-content-text")
text = element.text_content()
print(text)

words = text.split() 
#print(words)

words_lowercase = []
for word in words:
    words_lowercase.append(word.lower())
#print(words_lowercase)

counter = 0
for word in words_lowercase:
    if 'schumacher' in word:
        counter += 1

print(counter)









