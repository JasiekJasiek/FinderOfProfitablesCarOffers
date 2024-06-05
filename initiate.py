import sqlite3
import os

if os.path.isfile('otomoto.db') :
    os.unlink('otomoto.db')

from modules.DatabaseHandler import DatabaseHandler
from modules.Scraper import Scraper
from modules.Car import Car

conection = sqlite3.connect('otomoto.db')
database = conection.cursor()
database.execute("CREATE TABLE Cars(accident_free bool, brand varchar(255), course int, exploitation varchar(255), horse_power int, model varchar(255), price int, production_year int, URL varchar(255))")
conection.commit()
conection.close()

scraper = Scraper()

car = scraper.scrap('https://www.otomoto.pl/osobowe/oferta/volkswagen-golf-vw-golf-v-kombi-zadbany-13700-do-negocjacji-ID6Goruz.html')

DatabaseHandler.add_new_car_to_database(car, 'https://www.otomoto.pl/osobowe/oferta/volkswagen-golf-vw-golf-v-kombi-zadbany-13700-do-negocjacji-ID6Goruz.html')
