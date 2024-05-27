from bs4 import BeautifulSoup
import requests


class CarFinder:

    def __init__(self):
        self.response = requests.get("https://www.otomoto.pl/osobowe?search%5Border%5D=created_at_first%3Adesc")

    def look_for_new_car(self):
        soup = BeautifulSoup(self.response.text, "html.parser")
        offer1 = soup.find("h1")
        offer1 = str(offer1.find("a"))
        offer1 = offer1.removeprefix('<a href="')
        offer1 = offer1.removesuffix('.html*')
        url = offer1[0:url.find('"')]
        return(url)
