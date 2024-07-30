import csv
from typing import Dict


def read_cattle_data() -> Dict[str, Dict[int, int]]:
    cattle_data = {}
    with open('cattle_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            Name, Total_in_2022, Total_in_2021 = row[0], int(row[1]), int(row[2])
            cattle_data[Name] = {
                2021: Total_in_2021,
                2022: Total_in_2022
            }

    return cattle_data