from typing import Dict

import csv

from fastapi import APIRouter, Depends, HTTPException

from ..dictionary.dictionarycattle_data import read_cattle_data

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/cattle",
    tags=["cattle"],
    responses={404: {"description": "Not found"}},
)


@router.get("/total/{year}")
async def get_total_cattle_by_year(year: int):
    try:
        total_cattle_by_department = {}
        with open("dictionarycattle_data.py", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row["year"]) == year:
                    department = row["department"]
                    total_cattle = int(row["total_cattle"])
                    if department in total_cattle_by_department:
                        total_cattle_by_department[department] += total_cattle
                    else:
                        total_cattle_by_department[department] = total_cattle
        return total_cattle_by_department
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Cattle data file not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))