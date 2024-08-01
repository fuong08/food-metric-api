from typing import List, Dict
# import csv

# import dic
from fastapi import APIRouter, Depends, HTTPException

# from .. import dictionary
from ..dictionary.cattle_data import read_cattle_data
from ..dependencies import get_token_header

router = APIRouter(
    prefix="/cattle",
    tags=["cattle"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_items_db = {"columbia": {"name": "columbia"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items():
    return fake_items_db


@router.get("/total_year")
async def get_total_cattle_by_year(year: int) -> dict:
    if year not in [2022, 2021]:
        raise HTTPException(status_code=404, detail=f"Year {year} not found.")

    data = read_cattle_data()
    result = dict()
    result["data"] = dict()

    if year == 2021:
        result["year"] = 2021
        for key in data.keys():
            result["data"][key] = data[key][2021]
    else:
        result["year"] = 2022
        for key in data.keys():
            result["data"][key] = data[key][2022]

    return result


@router.put(
    "/total_year",
    tags=["cattle"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return dict(total_cattle=get_total_cattle_by_year)
