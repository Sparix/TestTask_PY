from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/w/index.php?title=List_of_countries_by_population_(United_Nations)&oldid=1215058959"


@dataclass
class Country:
    name: str
    population: int
    region: str


class CountryParser:
    def __init__(self, url):
        self.url = url

    def get_page(self):
        response = requests.get(self.url).content
        soup = BeautifulSoup(response, "html.parser")
        return soup

    def page_find_countries(self, soup: BeautifulSoup):
        table = soup.select("table > tbody > tr")
        countries = []
        for line in table:
            if line.select_one("tr > td > span.datasortkey > a"):
                countries.append(Country(
                    name=line.select_one("tr > td > span.datasortkey > a").text,
                    population=(
                        int(
                            line.select("tr > td")[2].text.replace(",", "")
                        )
                        if line.select("tr > td")[2].text != "N/A"
                        else None
                    ),
                    region=line.select("tr > td")[4].select_one("a").text
                ))
        return countries

    def parse(self):
        soup = self.get_page()
        return self.page_find_countries(soup)


def main_scrapper():
    parser = CountryParser(URL)
    countries = parser.parse()
    return countries
