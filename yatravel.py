#!/etc/bin python3
import time

from get_rating.csv_utils import read_csv_file, write_csv_file
from get_rating.rating_utils import get_ya_travel_ratting

def main():
    hotel_yatravel_dict = read_csv_file("get_rating/docs/read_file/yatravel.csv")

    count = 0
    for hotel in hotel_yatravel_dict:
        try:
            hotel["rating"] = get_ya_travel_ratting(hotel["URL"])
        except:
            hotel["rating"] = "No rating"
            time.sleep(1)
        count += 1
        print(count, hotel)

    write_csv_file(hotel_yatravel_dict, "get_rating/docs/ya_rating.csv")


if __name__=="__main__":
    main()


