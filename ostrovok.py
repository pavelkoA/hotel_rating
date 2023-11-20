#!/etc/bin python3
import time
import csv
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import random


def read_csv_file(read_doc_path="get_rating\\docs\\read_file\\ostrovok.csv.csv") -> list:
    hotels_data_list = []
    with open(read_doc_path, "r", encoding="utf-8-sig") as exel:
        file = csv.DictReader(exel, delimiter=",",)
        for row in file:
            hotels_data_list.append(row)
    return hotels_data_list


proxy1 = {
    'https': 'socks5://vAcqzZ:8ZeV5m@31.44.190.36:9421',
    'http': 'socks5://vAcqzZ:8ZeV5m@31.44.190.36:9421'
}


proxy2 = {
    'https': 'socks5://vAcqzZ:8ZeV5m@31.44.190.20:9746',
    'http': 'socks5://vAcqzZ:8ZeV5m@31.44.190.20:9746'
}


proxy3 = {
    'https': 'socks5://vAcqzZ:8ZeV5m@31.44.188.6:9981',
    'http': 'socks5://vAcqzZ:8ZeV5m@31.44.188.6:9981'
}


proxy_list = [proxy1, proxy2, proxy3]


ua = UserAgent()


headers = {
    "User-Agent": ua.random
}


def get_requests_hotel_site(link):
    """return requests.text object"""
    hotel_requests = requests.get(link,
                                  headers=headers)
    return hotel_requests.text


def get_hotel_page_soup(link):
    """return beautiful soup object for rating functions"""
    hotel_requests = get_requests_hotel_site(link)
    hotel_page_soup = BeautifulSoup(hotel_requests, "lxml")
    return hotel_page_soup


def get_ostrovok_rating(link):
    """Get hotel rating ostrovok.ru"""
    hotel_page_soup = get_hotel_page_soup(link)
    hotel_rating_value = hotel_page_soup.find(
        "span", class_="TotalRating_content__k5u6S")
    if hotel_rating_value:
        return hotel_rating_value.text


def main():
    hotel_ostrovok_dict = read_csv_file("get_rating/docs/read_file/ostrovok.csv")
    with open("get_rating/docs/ostrovok_rating.csv", "w",
              encoding="utf-8-sig", newline='') as write_file:
        fieldnames_list = [key for key in hotel_ostrovok_dict[0].keys()]
        writer = csv.DictWriter(write_file, fieldnames=fieldnames_list, delimiter=",")
        writer.writeheader()
        count = 0
        for hotel in hotel_ostrovok_dict:
            try:
                hotel["rating"] = get_ostrovok_rating(hotel["URL"])
            except:
                hotel["rating"] = "No rating"
                time.sleep(1)
            writer.writerow(hotel)
            count += 1
            print(count, hotel)


if __name__ == "__main__":
    main()
