from modules.Car import Car
from modules.CarFinder import CarFinder
from modules.ChartMaker import ChartMaker
from modules.DatabaseHandler import DatabaseHandler
from modules.EmailSender import EmailSender
from modules.Scraper import Scraper
from time import sleep
import statistics

def worth_of_car(car: Car) -> int:
    def accident_free(car: Car) -> bool:
        if car.accident_free == '1':
            return True
        return False
    def points_for_price(car: Car) -> int:
        prices = DatabaseHandler.get_prices_for_similar_car(car)
        avarage = statistics.mean(prices)
        if int(car.price) <= 0.85*avarage:
            return 20
        if int(car.price) <= 0.9*avarage:
            return 15
        if int(car.price) <= avarage:
            return 10
        if int(car.price) <= 1.05*avarage:
            return 5
        else:
            return 0

    def points_for_course(car: Car) -> int:
        courses = DatabaseHandler.get_courses_for_similar_car(car)
        median = statistics.median(courses)
        if int(car.course) <= 0.85*median:
            return 20
        if int(car.course) <= 0.9*median:
            return 15
        if int(car.course) <= median:
            return 10
        if int(car.course) <= 1.05*median:
            return 5
        else:
            return 0

    def points_for_year(car: Car) -> int:
        year = int(car.production_year)
        if year >= 2014:
            return 10
        return 10 - (2014 - year)
    
    points = 0
    
    if accident_free(car):
        points += 50 

    points += points_for_price(car)
    points += points_for_course(car)
    points += points_for_year(car)
    if points < 70:
        return 0
    if points>=70 and points<=85:
        return 1
    else:
        return 2


email = input('Please type your email :')
finder = CarFinder()
scraper = Scraper()
while True:
    
    sleep(60)
    url = finder.look_for_new_car()
    
    if url == None:
        continue

    car = scraper.scrap_car_atributes(url)
    car_category = worth_of_car(car)

    if car_category:
        ChartMaker.make_course_chart(DatabaseHandler.get_courses_for_similar_car(car), int(car.course))
        ChartMaker.make_price_chart(DatabaseHandler.get_prices_for_similar_car(car), int(car.price))
        EmailSender.send_email(email,url,car_category)
    
    DatabaseHandler.add_new_car_to_database(car,url)
