from fake_useragent import UserAgent
from get_rating.csv_utils import read_csv_file, write_csv_file
from get_rating.rating_utils import get_level_travel_rating

def main():
    hotel_leaveltravel_dict = read_csv_file("get_rating/docs/read_file/leaveltravel.csv")
    
    count = 0
    for hotel in hotel_leaveltravel_dict:
        hotel["rating"] = get_level_travel_rating(hotel["URL"])
        count += 1
        print(f"{count}) {hotel['URL']} - {hotel['rating']}")
    write_csv_file(hotel_leaveltravel_dict)


if __name__=="__main__":
    main()


