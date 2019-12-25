'''
https://www.google.com.ua/search
?sxsrf=ACYBGNQCCdvQTRfkX4ZDJzKWa7rc0VFP7A:1576601751223
&source=hp
&ei=lwj5XfaBC-n2qwHLt4GACA
&q=cat
&oq=
&gs_l=psy-ab.1.0.35i362i39l10.0.0..34132...3.0..0.0.0.......0......gws-wiz.....10.M_vJevle9is
&safe=images
'''

import requests
import bs4

template = "https://google.com?q={}"
page = requests.get(template.format("cat"))

bs_page = bs4.BeautifulSoup(page.text, "html.parser")

print(bs_page.text)

bs_page = bs4.BeautifulSoup(page.text, "html.parser")
print("="*40)
print(bs_page.get_text())