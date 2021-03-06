from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

class MovieChecker:
    def __init__(self, config):
        self.CHROME_DRIVER_PATH = config.get_chrome_driver_path()
        self.PREMIER_DATE = config.get_premier_date()
        self.MAIN_URL = config.get_imax_url()
        self.MOVIE = config.get_movie_title()
        
        self.CHROME_DRIVER_OPTIONS = Options()
        self.CHROME_DRIVER_OPTIONS.add_argument('--headless')

    def check_movie(self):
        driver = webdriver.Chrome()
        driver.get(self.MAIN_URL)
        if self.PREMIER_DATE not in driver.current_url:
            print("Movies are not presented for this date yet: " + self.PREMIER_DATE)
            driver.quit()
            return False
        elements = driver.find_elements_by_class_name("movie-row")
        for element in elements:
            movie = element.find_element_by_xpath(".//h4[@class='qb-movie-name']").text
            movie = movie.lower().strip()
            if self.MOVIE in movie:
                print("Found movie: " + movie)
                driver.quit()
                return True
            print("Movies are presented on given date but selected one is not found: " + self.MOVIE)
            driver.quit()
            return False
