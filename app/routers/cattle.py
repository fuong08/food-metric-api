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

async def get_total_cattle_by_year(year: int) -> List[dictionary]:
    if year not in [2022, 2021]:
        raise HTTPException(status_code=404, detail=f"Year {year} not found.")

    if year == 2022:
        return dictionary
    else:
        return dictionary

    if year == 2021:
        return dictionary
    else:
        return dictionary