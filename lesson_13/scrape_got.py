from urllib2 import urlopen
from bs4 import BeautifulSoup


def get_got_viewers():
    total_viewers = 0.0
    base_url = "https://en.wikipedia.org"
    initial_url = base_url + "/wiki/Game_of_Thrones"
    response = urlopen(initial_url).read()

    soup = BeautifulSoup(response, "html.parser")
    section_header = soup.find(id="Adaptation_schedule")
    table = section_header.parent.find_next_sibling("table")
    ths = table.find_all("th", attrs={"scope": "row"})

    for idx, th in enumerate(ths):
        print "Calculating season {} of {}".format(idx + 1, len(ths))

        season_url = base_url + th.find("a")["href"]
        season_response = urlopen(season_url).read()
        season_soup = BeautifulSoup(season_response, "html.parser")

        episodes_table = season_soup.find("table", attrs={"class": "wikiepisodetable"})

        episodes_rows = episodes_table.find_all("tr", attrs={"class": "vevent"})

        for row in episodes_rows:
            episode_viewers_data = row.find_all("td")[-1].strings

            episode_viewers = None
            for data in episode_viewers_data:
                try:
                    episode_viewers = float(data)

                except (ValueError, TypeError):
                    pass  # not the data we are looking for

            if episode_viewers:
                total_viewers += episode_viewers

    return total_viewers


def main():
    total_viewers = get_got_viewers()
    print "Total number of Game of Throne viewers in U.S. is {} millions".format(total_viewers)


if __name__ == '__main__':
    main()
