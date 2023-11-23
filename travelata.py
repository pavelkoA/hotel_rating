#!/etc/bin python3
import time
import csv
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def read_csv_file(read_doc_path="get_rating\\docs\\read_file\\travelata.csv") -> list:
    hotels_data_list = []
    with open(read_doc_path, "r", encoding="utf-8-sig") as exel:
        file = csv.DictReader(exel, delimiter=",",)
        for row in file:
            hotels_data_list.append(row)
    return hotels_data_list



req_dolphin = f'http://localhost:3001/v1.0/browser_profiles/' \
              f'{113400739}/start?automation=1'

port_dolphin = str(requests.get(req_dolphin).json()['automation']['port'])

chrome_driver_path = Service("C:\chromedriver\chromedriver\chromedriver-win-x64.exe")
options = webdriver.ChromeOptions()
options.debugger_address = '127.0.0.1:' + port_dolphin


def main():
    hotel_travelata_dict = read_csv_file("get_rating/docs/read_file/travelata.csv")
    with open("get_rating/docs/travelata_rating.csv", "w",
              encoding="utf-8-sig", newline='') as write_file:
        fieldnames_list = [key for key in hotel_travelata_dict[0].keys()]
        writer = csv.DictWriter(write_file, fieldnames=fieldnames_list, delimiter=",")
        writer.writeheader()
        with webdriver.Chrome(service=chrome_driver_path, options=options) as browser:
            count = 0
            for hotel in hotel_travelata_dict[::100]:
                browser.get(hotel["URL"])
                browser.refresh()
                try:
                    hotel["rating"] = browser.find_element(By.CSS_SELECTOR,
                                            '[itemprop="ratingValue"]').text
                except:
                    hotel["rating"] = 'no rating'
                    time.sleep(1)
                writer.writerow(hotel)
                count += 1
                print(count, hotel)


if __name__ == "__main__":
    main()