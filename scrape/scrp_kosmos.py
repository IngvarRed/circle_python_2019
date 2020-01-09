# scrape https://liniakino.com/showtimes/kosmos/

import os
import bs4
# from bs4 import BeautifulSoup
import requests
import time

start_url = "http://liniakino.com/showtimes/kosmos/"

with open("data.csv", "w") as f:

    main_page = requests.get(start_url)
    main_page_bs = bs4.BeautifulSoup(main_page.text, "html.parser")
    show_times = main_page_bs.find_all('li', {'class': 'showtime-movie'})

    for num, show_time in enumerate(show_times):
        print('\n>>>>> start <<<<<')
        line = ''
        name = show_times[num].find('h1')
        name_l = name.get_text().strip()
        print(name_l)
        line += '\"' + name_l + '\",'

        day_blocks = show_times[num].find_all('div', {'class': 'day-block showtime-day'})
        for day_block in day_blocks:
            datt = day_block.find('label', {'class': 'date'})
            print(datt.get_text().strip().replace(',', '-'))
            line += datt.get_text().strip().replace(',', '-') + ','

            ul_show_times = day_block.find_all('ul', {'class': 'showtime-time'})
            for ul_show_time in ul_show_times:
                film_times = ul_show_time.find_all("li", {"class": 'showtime-item'})
                for timm in film_times:
                    print(timm.a.get_text())
                    line += timm.a.get_text() + ','


        poster = show_times[num].find('div', {'class': 'poster'})
        print(poster.a.img['src'])
        img_url = poster.a.img['src']
        img_data = requests.get(img_url, stream=True)
        base_dir = os.path.dirname(__file__)
        # file_name = os.path.join(base_dir, "img", name_l.replace(" ", "_") + ".jpg")
        file_name = base_dir + '/' + "img/" + name_l.replace(" ", "_") + ".jpg"
        with open(file_name, "bw") as f_image:
            f_image.write(img_data.content)

        line += file_name
        print(line)
        f.write(line + "\n")

        print('>>>>> finish <<<<<')