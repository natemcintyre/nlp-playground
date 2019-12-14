# https://towardsdatascience.com/gentle-start-to-natural-language-processing-using-python-6e46c07addf3

# Fetch data via a url request and read the data
import urllib.request
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()
print(html)

# Clean the html content parsing it down to just raw text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html5lib')
text = soup.get_text(strip = True)
print(text)

# Tokenize the text content
tokens = [t for t in text.split()]
print(tokens)

# Count word frequency from the tokenized content
import nltk
from nltk.corpus import stopwords
sr = stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
        if token in stopwords.words('english'):
            clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)

for key,value in freq.items():
    print(str(key) + ': ' + str(value))

freq.plot(20, cumulative=False)
