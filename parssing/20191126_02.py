#
import requests
import bs4

responce = requests.get("http://quotes.toscrape.com/")

# print(responce.text)

soup = bs4.BeautifulSoup(responce.text, 'html.parser')
print(soup.title.string)
divs = soup.find_all("div", {"class": "quote"})
print(len(divs))

#print(divs)
#exit(0)
for n, link in enumerate(divs):
    print("-"*10, n, "-"*10)
    print(link.span.text)
    print(link.find('small', {'class': 'author'}).text)


