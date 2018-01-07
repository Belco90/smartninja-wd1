from urllib2 import urlopen
from bs4 import BeautifulSoup


class ScrapeBookProfile(object):
    def __init__(self, name, email, city):
        self.name = name
        self.email = email
        self.city = city

    def get_csv_line(self):
        return ",".join([self.name, self.email, self.city]) + "\n"


url = 'https://scrapebook22.appspot.com'
response = urlopen(url).read()

soup = BeautifulSoup(response, "html.parser")
profiles = []

for link in soup.find_all("a"):
    if link.string == "See full profile":
        profile_link = url + link["href"]
        profile_response = urlopen(profile_link).read()
        profile_soup = BeautifulSoup(profile_response, "html.parser")

        email = profile_soup.find("span", attrs={"class": "email"}).string
        name = profile_soup.find("div", attrs={"class": "row"}).find("h1").string
        data_list = profile_soup.find("div", attrs={"class": "row"}).find("ul").find_all("span")
        city = ""
        for item in data_list:
            if "data-city" in item.attrs:
                city = item.string

        profiles.append(ScrapeBookProfile(name=name, email=email, city=city))

with open("scrape_book_profiles.csv", "w+") as csv_file:
    for idx, profile in enumerate(profiles):
        print "saving {} of {}".format(idx + 1, len(profiles))
        csv_file.write(profile.get_csv_line())
