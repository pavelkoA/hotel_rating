import csv


def read_csv_file(doc_path) -> list:
    hotels_data_list = []
    with open(doc_path, "r", encoding="utf-8-sig") as exel:
        file = csv.DictReader(exel, delimiter=",",)
        for row in file:
            hotels_data_list.append(row)
    return hotels_data_list


path = 'docs\\SERP.csv'
print(read_csv_file(path))
