import csv

with open('docs/SERP.csv', "r", encoding="utf-8", newline="") as exel:
    file = csv.reader(exel, delimiter=";")
