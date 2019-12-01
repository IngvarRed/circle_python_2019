#
import requests
import bs4

url = ""
start_url = "http://quotes.toscrape.com"

while True:
    print(url)
    url = start_url + url
    responce = requests.get(url)
    # print(responce.text)
    soup = bs4.BeautifulSoup(responce.text, 'html.parser')
    for item in soup.find_all('div', {'class': 'quote'}):
        print(item.span.text)
        print(item.find('small', {'class': 'author'}).text)

    li = soup.find('li', {'class': 'next'})
    if li is None:
        break
    a = li.a
    url = a['href']
