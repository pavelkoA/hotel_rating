from get_rating.csv_utils import read_csv_file, write_csv_file
from get_rating.rating_utils import (get_level_travel_rating, get_ya_travel_ratting,
                                     get_ostrovok_rating, get_travelata_rating)
import asyncio
from copy import deepcopy

def collect_ostrovok_rating(hotel_data_dict):
    ostrovok_link = hotel_data_dict["ostrovok.ru"]
    return get_ostrovok_rating(ostrovok_link)


def collect_level_travel_rating(hotel_data_dict):
    level_travel_link = hotel_data_dict["level.travel"]
    return get_level_travel_rating(level_travel_link)


def collect_travelata_rating(hotel_data_dict):
    travelata_link = hotel_data_dict["travelata.ru"]
    return get_travelata_rating(travelata_link)


def collect_travel_yandex_rating(hotel_data_dict):
    travel_yandex_link = hotel_data_dict["travel.yandex.ru"]
    return get_ya_travel_ratting(travel_yandex_link)


def get_hotels_dict(hotel):
    try:
        hotel["rating_ostrovok.ru"] = collect_ostrovok_rating(hotel)
        hotel["rating_level.travel"] = collect_level_travel_rating(hotel)
        hotel["rating_travelata.ru"] = collect_travelata_rating(hotel)
        hotel["rating_travel.yandex.ru"] = collect_travel_yandex_rating(hotel)
        print(hotel["rating_ostrovok.ru"], hotel["rating_level.travel"], hotel["rating_travelata.ru"], hotel["rating_travel.yandex.ru"])
        return hotel
    except:
        return None

def collect_all_rating():
    read_file_hotels: list = read_csv_file()
    write_file_hotels: list = []
    for hotel in read_file_hotels:
        hot = ''
        while not hot:
            hot = get_hotels_dict(hotel)
            write_file_hotels.append(hot)
    write_csv_file(write_file_hotels)
