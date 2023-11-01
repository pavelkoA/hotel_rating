import csv


def read_csv_file(read_doc_path="..\\docs\\read_file\\SERP.csv") -> list:
    hotels_data_list = []
    with open(read_doc_path, "r", encoding="utf-8-sig") as exel:
        file = csv.DictReader(exel, delimiter=",",)
        for row in file:
            hotels_data_list.append(row)
    return hotels_data_list


def write_csv_file(hotels_data_list_dict: list,
                   hotels_rating_file_path="..\\docs\\hotels_rating.csv"):
    with open(hotels_rating_file_path, "w",
              encoding="utf-8-sig", newline='') as write_file:
        if hotels_data_list_dict:
            fieldnames_list = [key for key in hotels_data_list_dict[0].keys()]
        writer = csv.DictWriter(write_file, fieldnames=fieldnames_list, delimiter=",")
        writer.writeheader()
        for row in hotels_data_list_dict:
            writer.writerow(row)
