import matplotlib.pyplot as plt
import statistics

class ChartMaker:

    @staticmethod
    def make_price_chart(prices: list[int], offer_price: int) -> None:
        avg_price = sum(prices) / len(prices)
        prices.sort()
        plt.scatter( [i for i in range(len(prices))], prices, label='Offers from Database')
        plt.axhline(y=avg_price, color='r', linestyle='-', label=f'Avg price = {avg_price:.0f} PLN')
        plt.axhline(y=offer_price, color='y', linestyle='--', label=f'This offer price = {offer_price:.0f} PLN')
        plt.title('Price distribution')
        plt.xlabel('Index')
        plt.ylabel('Price')
        plt.legend()
        plt.savefig('resources/price_chart.jpg')  
        plt.clf()
        
    @staticmethod
    def make_course_chart(courses: list[int], offer_course: int) -> None:
        median_course = statistics.median(courses)
        courses.sort()
        plt.scatter( [i for i in range(len(courses))], courses, label='Offers from Database')
        plt.axhline(y=median_course, color='r', linestyle='-', label=f'Avg course = {median_course:.0f} PLN')
        plt.axhline(y=offer_course, color='y', linestyle='--', label=f'This offer course = {offer_course:.0f} PLN')
        plt.title('Course distribution')
        plt.xlabel('Index')
        plt.ylabel('Course')
        plt.legend()
        plt.savefig('resources/course_chart.jpg') 
        plt.clf() 
