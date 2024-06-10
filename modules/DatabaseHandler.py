import sqlite3
from modules.Car import Car
from modules.Scraper import Scraper
import math

class DatabaseHandler:
    
    connection = sqlite3.connect('resources/otomoto.db')
    database = connection.cursor()
    
    @staticmethod
    def is_already_in_database(URL: str) -> bool:
        DatabaseHandler.database.execute(f"SELECT Count(*) FROM Cars WHERE URL = '{URL}'")
        response = DatabaseHandler.database.fetchall()
        if response[0][0] == 1:
            return True
        return False
    
    @staticmethod
    def add_new_car_to_database(car: Car, URL: str) -> None:
        db_row = car.to_list()
        db_row.append(URL)
        DatabaseHandler.database.execute("INSERT INTO Cars VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", db_row)
        DatabaseHandler.connection.commit()

    @staticmethod
    def get_prices_for_similar_car(car: Car) -> list[int]:
        DatabaseHandler.database.execute(f"""
                                        SELECT price 
                                        FROM Cars 
                                        WHERE brand = '{car.brand}' AND 
                                              model = '{car.model}' AND 
                                              production_year <= '{int(car.production_year) + 1}' AND 
                                              production_year >= '{int(car.production_year) - 1}' AND
                                              horse_power <= '{int(car.horse_power) + 20}' AND
                                              horse_power >= '{int(car.horse_power) - 20}'
                                        """)
        response = DatabaseHandler.database.fetchall()
        return [ int(line[ 0 ]) for line in response]
    
    @staticmethod
    def get_courses_for_similar_car(car: Car) -> list[int]:
        DatabaseHandler.database.execute(f"""
                                        SELECT course 
                                        FROM Cars 
                                        WHERE brand = '{car.brand}' AND 
                                              model = '{car.model}' AND 
                                              production_year <= '{int(car.production_year) + 1}' AND 
                                              production_year >= '{int(car.production_year) - 1}' AND
                                              horse_power <= '{int(car.horse_power) + 20}' AND
                                              horse_power >= '{int(car.horse_power) - 20}'
                                        """)
        response = DatabaseHandler.database.fetchall()
        return [ int(line[ 0 ]) for line in response]
    
    
