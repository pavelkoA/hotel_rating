#!/etc/bin python3
import time
import csv
import json
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import random

from get_rating.csv_utils import read_csv_file


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


mob_proxy = {
    'https': 'https://Neuyp6:Ag2DuC9ZaY6a@zproxy.site:12505'
}


proxy_list = [proxy1, proxy2, proxy3]


def get_requests_hotel_site(link):
    """return requests.text object"""
    hotel_requests = requests.get(link,
                                  headers=headers,
                                  proxies=mob_proxy)
    return hotel_requests.text


def get_hotel_page_soup(link):
    """return beautiful soup object for rating functions"""
    hotel_requests = get_requests_hotel_site(link)
    hotel_page_soup = BeautifulSoup(hotel_requests, "lxml")
    return hotel_page_soup


def get_ya_travel_ratting(link):
    """Get hotel rating travelata.ru"""
    for _ in range(10):
        hotel_page_soup = get_hotel_page_soup(link)
        hotel_rating_value = hotel_page_soup.find("script", type="application/ld+json")
        if hotel_rating_value:
            rating = json.loads(hotel_rating_value.text)
            try:
                return rating["aggregateRating"]["ratingValue"]
            except KeyError:
                return "no rating"
        time.sleep(2)
    return "no rating"


def main():
    hotel_yatravel_dict = read_csv_file("get_rating/docs/read_file/yatravel.csv")
    with open("get_rating/docs/yatravel_rating.csv", "w",
              encoding="utf-8-sig", newline='') as write_file:
        fieldnames_list = [key for key in hotel_yatravel_dict[0].keys()]
        writer = csv.DictWriter(write_file, fieldnames=fieldnames_list, delimiter=",")
        writer.writeheader()
        count = 0
        for hotel in hotel_yatravel_dict:
            try:
                hotel["rating"] = get_ya_travel_ratting(hotel["URL"])
            except:
                hotel["rating"] = "No rating"
                time.sleep(1)
            writer.writerow(hotel)
            count += 1
            print(count, hotel)


if __name__=="__main__":
    main()


