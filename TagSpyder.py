import requests
import csv
import os
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

class TagSpyder:
    def __init__(self):
        self.driver = None

    url_list = []

    def parseCSVData(self):
        with open('Tags.csv','r') as csvRead:
            for urls in csvRead:
                self.url_list.append(urls)

    @staticmethod
    def get_driver_path():
        path = os.path.dirname(os.path.realpath(__file__))
        bin_path = os.path.join(path,'chromedriver')
        return bin_path

    @staticmethod
    def get_chrome_options():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        return options

    def hit_url(self):
        self.parseCSVData()
        for i in self.url_list:
            r = requests.get(i)
            print r.status_code

    # def start_driver(self):
    #     try:
    #         chrome_bin_path = self.get_driver_path()
    #         chromeOptions = self.get_chrome_options()
    #         self.driver = webdriver.Chrome(
    #             executable_path=chrome_bin_path,
    #             chrome_options=chromeOptions
    #         )
    #     except WebDriverException as e:
    #         print e
    #
    # def close_driver(self):
    #     self.driver.quit()
    #
    # def get_page(self):
    #     response = self.hit_url()
    #     print response
        # if response == 200:
        #     self.driver.get(str(urls)
        #     self.driver.implicitly_wait(4)
        #     print self.driver.title
        # else:
        #     self.driver.quit()

#     def parse_info(self):
#         self.start_driver()
#         self.get_page()
#         self.close_driver()
#
ts = TagSpyder()
ts.hit_url()
