from bs4 import BeautifulSoup
import requests

class CarFinder:

    def __init__(self):
        self.response = requests.get('https://www.otomoto.pl/osobowe?search%5Border%5D=created_at_first%3Adesc')

    def extract_url_from_html_tag (self, html_tag):
        html_tag = html_tag.removeprefix('<a href="')
        return html_tag[0:html_tag.find('"')]
    
    def look_for_new_car(self):
        soup = BeautifulSoup(self.response.text, 'html.parser')
        first_offer_url = soup.find('h1')
        first_offer_url= str(first_offer_url.find('a'))
        return self.extract_url_from_html_tag(first_offer_url)
