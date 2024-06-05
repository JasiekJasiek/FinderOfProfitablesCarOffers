from bs4 import BeautifulSoup
import requests
from modules.DatabaseHandler import DatabaseHandler
from time import sleep

class CarFinder:

    def __init__(self):
        self.base_url = 'https://www.otomoto.pl/osobowe?search%5Border%5D=created_at_first%3Adesc'
        
    def extract_url_from_html_tag (self, html_tag):
        html_tag = html_tag.removeprefix('<a href="')
        return html_tag[0:html_tag.find('"')]
    
    def look_for_new_car(self):
        self.response = requests.get(self.base_url)
        soup = BeautifulSoup(self.response.text, 'html.parser')
        first_offer_url = soup.find('h1')
        if first_offer_url is None:
            sleep(5)
            return self.look_for_new_car()
        first_offer_url= str(first_offer_url.find('a'))
        url = self.extract_url_from_html_tag(first_offer_url)
        if DatabaseHandler.is_already_in_database(url):
            return None
        else:
            return url
        
