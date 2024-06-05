from bs4 import BeautifulSoup
import requests
from modules.Car import Car

class Scraper:

    def __init__(self) -> None:
        self.headers = self.read_file('./resources/headers.txt')
        self.ang_headers = self.read_file('./resources/ang_headers.txt')
        self.dictionary = self.make_dictionary(self.headers, self.ang_headers)

    def make_dictionary(self, keys: list[str], values: list[str]) -> dict[str, str]:
        dictionary = {}
        for i in range(len(keys)):
            dictionary[ keys[ i ] ] = values[ i ]
        return dictionary

    def read_file(self, URL: str) -> list[str]:
        with open(URL, 'r') as file:
            lines = file.readlines()
        return [line.removesuffix('\n') for line in lines]
    
    def remove_headers(self, s: str):
        for header in self.headers:
            value = s.replace(header, '')
            if s.find(header) != -1:
                return (self.dictionary[ header ], value)
            
    def how_many_nones(self, arr: list[ tuple[ str, str ] ]):
        cnt = 0
        for item in arr:
            if item == None:
                cnt += 1
        return cnt

    def remove_none(self, arr: list[tuple[str, str]]) -> None:
        cnt = self.how_many_nones(arr)
        for _ in range(cnt):
            arr.remove(None)

    def convert_accident_free(self, atribute: str) -> str:
        if atribute == 'Null':
            return 'Null'
        if atribute == 'tak':
            return '1'
        else:
            return '0'
        
    def convert_exploitation(self, atribute: str) -> str:
        if atribute == 'używane':
            return 'used'
        else:
            return 'new'

    def adjust_atributes(self, atributes: list[tuple[str, str]]):
        dictionary = {}
        for [header, value] in atributes:
            dictionary[ header ] = (value.lower().replace(' km', '').replace(' ', ''))
        values = [('price', dictionary[ 'price' ])]
        for header in self.headers:
            if not dictionary.__contains__(self.dictionary[ header ]):
                dictionary[ self.dictionary[ header ] ] = 'Null'
        for header in self.headers:
            values.append((self.dictionary[ header ], dictionary[ self.dictionary[ header ] ]))
        values.sort(key= lambda x: x[0])
        values_res = [value for [header, value] in values]
        return (self.convert_accident_free(values_res[ 0 ]), values_res[ 1 ], values_res[ 2 ], self.convert_exploitation(values_res[ 3 ]), values_res[ 4 ], values_res[ 5 ], values_res[ 6 ], values_res[ 7 ])

    def scrap(self, URL: str) -> Car:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        atributes = soup.find_all(class_ = 'ooa-162vy3d e18eslyg3')
        atributes = [ self.remove_headers(atribute.text) for atribute in atributes]
        atributes.append(('price', soup.find(class_ = 'offer-price__number eqdspoq4 ooa-o7wv9s er34gjf0').text.replace(' ', '')))
        self.remove_none(atributes)
        atributes = self.adjust_atributes(atributes)
        return Car(atributes)
