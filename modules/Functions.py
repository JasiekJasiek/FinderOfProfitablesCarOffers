from bs4 import BeautifulSoup
import requests

def get_soup(URL: str) -> BeautifulSoup:
    page = requests.get(URL)
    return BeautifulSoup(page.text, 'html.parser')
