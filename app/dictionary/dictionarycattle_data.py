import csv
from typing import Dict


def read_cattle_data() -> Dict[str, int]:
    cattle_data = {}
    with open('datacattle.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            Department, Total_in_2022, Total_in_2021 = row[0], int(row[1]), int(row[2])

    return cattle_data
