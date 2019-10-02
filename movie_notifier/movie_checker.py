from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import os

class MovieChecker:
    def __init__(self, config):
        self.PREMIER_DATE = config.get_premier_date()
        self.MAIN_URL = config.get_imax_url()
        self.MOVIE = config.get_movie_title()

    def check_movie(self):
        with urllib.request.urlopen(self.MAIN_URL) as response:
            html = response.read().decode('utf-8')
            print(html)
        #print(response.url); print(response.text)
        '''if self.MAIN_URL != driver.current_url:
            print("Movies are not presented for this date yet: " + self.PREMIER_DATE)
            return False
        elements = driver.find_elements_by_class_name("movie-row")
        for element in elements:
            movie = element.find_element_by_xpath(".//h4[@class='qb-movie-name']").text
            movie = movie.lower().strip()
            if self.MOVIE in movie:
                print("Found movie: " + movie)
                return True
            print("Movies are presented on given date but selected one is not found: " + self.MOVIE)
            return False
        driver.quit()'''
