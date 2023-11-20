#!/etc/bin python3
from get_rating.csv_utils import read_csv_file, write_csv_file
from get_rating.rating_utils import get_level_travel_rating

def main():
    hotel_leaveltravel_dict = read_csv_file("get_rating/docs/read_file/leaveltravel.csv")

    count = 0
    for hotel in hotel_leaveltravel_dict:
        hotel["rating"] = "Error"
        while hotel["rating"] == "Error":
            try:
                hotel["rating"] = get_level_travel_rating(hotel["URL"])
            except:
                hotel["rating"] = "Error"
        count += 1
        print(count, hotel)

    write_csv_file(hotel_leaveltravel_dict, "get_rating/docs/hotels_rating.csv")


if __name__=="__main__":
    main()


