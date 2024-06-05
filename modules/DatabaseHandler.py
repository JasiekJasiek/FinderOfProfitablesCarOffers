import sqlite3
from modules.Car import Car
from modules.Scraper import Scraper

class DatabaseHandler:
    
    connection = sqlite3.connect('otomoto.db')
    database = connection.cursor()
    
    @staticmethod
    def is_already_in_database(URL) -> bool:
        DatabaseHandler.database.execute(f"SELECT Count(*) FROM Cars WHERE URL = '{URL}'")
        response = DatabaseHandler.database.fetchall()
        if response[0][0] == 1:
            return True
        return False
    
    @staticmethod
    def add_new_car_to_database(car: Car, URL) -> None:
        db_row = car.to_list()
        db_row.append(URL)
        DatabaseHandler.database.execute("INSERT INTO Cars VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", db_row)
        DatabaseHandler.connection.commit()

  
