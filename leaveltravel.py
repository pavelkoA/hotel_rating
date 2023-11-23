#!/etc/bin python3
import time
import csv
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import random
from get_rating.csv_utils import read_csv_file, write_csv_file
from get_rating.rating_utils import get_level_travel_rating


ua = UserAgent()
headers = {
    "User-Agent": ua.random
}


proxy = {
        'https': 'socks5://q6G8yQ:xs33tk@146.19.234.45:8000',
        'http': 'socks5://q6G8yQ:xs33tk@146.19.234.45:8000'
    }


proxy1 = {
    'https': 'socks5://vAcqzZ:8ZeV5m@31.44.190.36:9421',
    'http': 'socks5://vAcqzZ:8ZeV5m@31.44.190.36:9421'
}

proxy2 = {
    'https': 'https://vAcqzZ:8ZeV5m@31.44.190.20:9746',
    'http': 'http://vAcqzZ:8ZeV5m@31.44.190.20:9746'
}
proxy3 = {
    'https': 'https://vAcqzZ:8ZeV5m@31.44.188.6:9981',
    'http': 'http://vAcqzZ:8ZeV5m@31.44.188.6:9981'
}


proxy_list = [proxy1, proxy2, proxy3]


def get_requests_hotel_site(link):
    """return requests.text object"""
    hotel_requests = requests.get(link,
                                  headers=headers,
                                  proxies=random.choice(proxy_list), timeout=5)
    return hotel_requests.text


def get_hotel_page_soup(link):
    """return beautiful soup object for rating functions"""
    hotel_requests = get_requests_hotel_site(link)
    hotel_page_soup = BeautifulSoup(hotel_requests, "lxml")
    return hotel_page_soup


def get_level_travel_rating(link):
    """Get hotels rating level.travel"""
    hotel_page_soup = get_hotel_page_soup(link)
    hotel_rating_value = hotel_page_soup.find("span",
                                              class_="hotel-rating-value")
    if hotel_rating_value:
        return hotel_rating_value.text


def main():
    hotel_leaveltravel_dict = read_csv_file("get_rating/docs/read_file/leaveltravel.csv")
    with open("get_rating/docs/leaveltravel_rating.csv", "w",
              encoding="utf-8-sig", newline='') as write_file:
        fieldnames_list = [key for key in hotel_leaveltravel_dict[0].keys()]
        writer = csv.DictWriter(write_file, fieldnames=fieldnames_list, delimiter=",")
        writer.writeheader()
        count = 0
        for hotel in hotel_leaveltravel_dict:
            try:
                hotel["rating"] = get_level_travel_rating(hotel["URL"])
                time.sleep(1)
            except:
                hotel["rating"] = "No rating"
                time.sleep(1)
            writer.writerow(hotel)
            count += 1
            print(count, hotel)


if __name__=="__main__":
    main()


