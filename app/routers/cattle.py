from typing import Dict

from fastapi import APIRouter, Depends, HTTPException

from ..dictionary.dictionarycattle_data import read_cattle_data

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/cattle",
    tags=["cattle"],
    responses={404: {"description": "Not found"}},
)

cattle_data = read_cattle_data()


@router.get("/total/{year}")
async def get_total_cattle_by_year(year: int) -> Dict[str, int]:
    if year not in cattle_data:
        raise HTTPException(status_code=404, detail=f"Data for year {year} not found.")
    return cattle_data[year]
