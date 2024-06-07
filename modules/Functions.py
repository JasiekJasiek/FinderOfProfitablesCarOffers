from bs4 import BeautifulSoup
import requests

#get soup class varable from given site
def get_soup(URL: str) -> BeautifulSoup:
    page = requests.get(URL)
    #sometimes page is empty
    if page.text == '':
        return get_soup
    return BeautifulSoup(page.text, 'html.parser')
