from bs4 import BeautifulSoup
import requests


class CarFinder:

    def __init__(self):
        self.response = requests.get("https://www.otomoto.pl/osobowe?search%5Border%5D=created_at_first%3Adesc")

    def look_for_new_car(self):
        soup = BeautifulSoup(self.response.text, "html.parser")
        offer1 = soup.find("h1")
        url = str(offer1.find("a"))
        url = url.removeprefix('<a href="')
        url = url.removesuffix('.html*')
        url = url[0:url.find('"')]
        return(url)