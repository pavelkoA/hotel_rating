import requests
from bs4 import BeautifulSoup
import json
from get_rating.headers_and_proxies import headers, mob_proxy, proxy_list
import time
import random


def get_requests_hotel_site(link):
    """return requests.text object"""
    hotel_requests = requests.get(link,
                                  headers=headers,
                                  proxies=random.choice(proxy_list))
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


def get_travelata_rating(link):
    """Get hotel rating travel.yandex.ru"""
    hotel_page_soup = get_hotel_page_soup(link)
    hotel_rating_value = hotel_page_soup.find("span",
                                              itemprop="ratingValue")
    if hotel_rating_value:
        return hotel_rating_value.text


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


def get_ostrovok_rating(link):
    """Get hotel rating ostrovok.ru"""
    hotel_page_soup = get_hotel_page_soup(link)
    hotel_rating_value = hotel_page_soup.find(
        "span", class_="TotalRating_content__k5u6S")
    if hotel_rating_value:
        return hotel_rating_value.text
