from random import shuffle
from urllib2 import urlopen
from bs4 import BeautifulSoup


NUMBER_OF_QUOTES = 5
url = 'http://quotes.yourdictionary.com/theme/marriage/'
response = urlopen(url).read()

soup = BeautifulSoup(response, "html.parser")

quotes = soup.find_all("p", attrs={"class": "quoteContent"})

shuffle(quotes)

for i in range(NUMBER_OF_QUOTES):
    print "{}. {}\n".format(i + 1, quotes[i].string)
