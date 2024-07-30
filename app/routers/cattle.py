from typing import List
import csv

from fastapi import APIRouter, Depends, HTTPException

from .. import dictionary
from ..dictionary.dictionarycattle_data import read_cattle_data
from ..dependencies import get_token_header

router = APIRouter(
    prefix="/cattle",
    tags=["cattle"],
    responses={404: {"description": "Not found"}},
)


@router.get("/total/{year}")

async def get_total_cattle_by_year(year: int) -> List[dic[int, int]]:
    if year not in [2022, 2021]:
        raise HTTPException(status_code=404, detail=f"Year {year} not found.")

    if year == 2022:
        return dictionary
    else:
        return dictionary

