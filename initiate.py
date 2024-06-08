import sqlite3
import os

if os.path.isfile('resources/otomoto.db') :
    os.unlink('resources/otomoto.db')

from modules.DatabaseHandler import DatabaseHandler
from modules.Scraper import Scraper
from modules.Car import Car
from modules.CarFinder import CarFinder
from modules.Functions import get_soup

def read_all_cars() -> list[str]:
    with open('resources/cars.txt', 'r') as f:
        cars = f.readlines()
    return [car.removesuffix('\n') for car in cars]

#create database
conection = sqlite3.connect('resources/otomoto.db')
database = conection.cursor()
database.execute("CREATE TABLE Cars(accident_free bool, brand varchar(255), course int, exploitation varchar(255), horse_power int, model varchar(255), price int, production_year int, URL varchar(255))")
conection.commit()
conection.close()

cars = read_all_cars()
finder = CarFinder()

base_url = 'https://www.otomoto.pl/osobowe/'
page_part_ulr = '?page='

all_cars_url = set()

curr_car = 1
#iterate through all car brands and extract all cars urls
for car in cars:

    curr_url = base_url + car + page_part_ulr + str(1)
    soup = get_soup(curr_url)
    pages_found = soup.find_all(class_ = 'ooa-g4wbjr e1y5xfcl0')
    if pages_found == []:
        page_number = 1 
    else:
        page_number = min(int(pages_found[-1].text), 500)

    for i in range(page_number):
        os.system('cls')
        print(f'Collecting cars from all brands: {curr_car}/{len(cars)}')
        print(f'Current brand: {car}')
        print(f'Current page: {i + 1}/{page_number}')
        curr_url = base_url + car + page_part_ulr + str(i)
        soup = get_soup(curr_url)
        cars_table = soup.find_all(class_ = 'ooa-10gfd0w e1i3khom1')
        cars_table = [car.find('a') for car in cars_table]
        cars_urls = [finder.extract_url_from_html_tag(str(car)) for car in cars_table]
        for url in cars_urls:
            all_cars_url.add(url)
    curr_car += 1
    
#scrap all cars atributes and save them in database
car_number = len(all_cars_url)
i = 1
scraper = Scraper()
for url in all_cars_url:
    os.system('cls')
    print(f'Collecting all cars atributes: {i}/{car_number}')
    i += 1
    car = scraper.scrap_car_atributes(url)
    DatabaseHandler.add_new_car_to_database(car, url)
