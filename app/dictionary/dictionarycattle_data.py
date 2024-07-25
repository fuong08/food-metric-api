import csv
from typing import Dict


def read_cattle_data() -> Dict[str, int]:
    cattle_data = {}
    with open('cattle_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            department, year, total_cattle = row[0], int(row[1]), int(row[2])
            if year not in cattle_data:
                cattle_data[year] = {}
            cattle_data[year][department] = total_cattle
    return cattle_data
