from bs4 import BeautifulSoup
import requests
from modules.Car import Car

class Scraper:

    def __init__(self):
        self.headers = self.read_file('./resources/headers.txt')
        self.ang_headers = self.read_file('./resources/ang_headers.txt')
        self.dictionary = self.make_dictionary(self.headers, self.ang_headers)

    def make_dictionary(self, keys, values):
        dictionary = {}
        for i in range(len(keys)):
            dictionary[ keys[ i ] ] = values[ i ]
        return dictionary

    def read_file(self, URL: str):
        with open(URL, 'r') as file:
            lines = file.readlines()
        return [line.removesuffix('\n') for line in lines]
    
    def remove_headers(self, s: str):
        for header in self.headers:
            value = s.replace(header, '')
            if s.find(header) != -1:
                return (self.dictionary[ header ], value)
            
    def how_many_nones(self, arr):
        cnt = 0
        for item in arr:
            if item == None:
                cnt += 1
        return cnt

    def remove_none(self, arr):
        cnt = self.how_many_nones(arr)
        for _ in range(cnt):
            arr.remove(None)

    def convert_accident_free(self, atribute):
        if atribute == 'Tak':
            return True
        else:
            return False
        
    def convert_exploitation(self, atribute):
        if atribute == 'używane':
            return 'used'
        else:
            return 'new'

    def adjust_atributes(self, atributes):
        atributes.sort(key= lambda x: x[0])
        values = []
        for [header, value] in atributes:
            values.append(value.lower().replace(' km', '').replace(' ', ''))
        
        return (self.convert_accident_free(values[ 0 ]), values[ 1 ], int(values[ 2 ]), self.convert_exploitation(values[ 3 ]), values[ 4 ], int(values[ 5 ]), int(values[ 6 ]), int(values[ 7 ]))

    def scrap(self, URL: str):
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        atributes = soup.find_all(class_ = 'ooa-162vy3d e18eslyg3')
        atributes = [ self.remove_headers(atribute.text) for atribute in atributes]
        atributes.append(('price', soup.find(class_ = 'offer-price__number eqdspoq4 ooa-o7wv9s er34gjf0').text.replace(' ', '')))
        self.remove_none(atributes)
        atributes = self.adjust_atributes(atributes)
        return Car(atributes)
        
