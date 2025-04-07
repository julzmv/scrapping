book_url = "https://www.gutenberg.org/cache/epub/2701/pg2701-images.html"

import requests
from bs4 import BeautifulSoup

response = requests.get(book_url)

book_content = response.text
soup = BeautifulSoup(book_content, features="html.parser")

content = soup.get_text()
print(content)


