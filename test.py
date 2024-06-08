from modules.DatabaseHandler import DatabaseHandler
import statistics
from modules.Car import Car
from modules.Scraper import Scraper
import matplotlib.pyplot as plt

scraper = Scraper()
prices = DatabaseHandler.get_prices_for_similar_car(scraper.scrap_car_atributes('https://www.otomoto.pl/osobowe/oferta/volkswagen-golf-golf-8-ID6G0bm1.html'))



year, price = DatabaseHandler.get_avg_price_for_similar_car_through_years(scraper.scrap_car_atributes('https://www.otomoto.pl/osobowe/oferta/volkswagen-golf-golf-8-ID6G0bm1.html'))


plt.hist(prices)

plt.show()