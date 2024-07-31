from typing import List, Dict
# import csv

# import dic
from fastapi import APIRouter, Depends, HTTPException

# from .. import dictionary
from ..dictionary.dictionarycattle_data import read_cattle_data
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


@router.get("/{total_year}")
async def get_total_cattle_by_year(year: int) -> Dict[str, Dict[int, int]]:
    if year == 2021:
        return read_cattle_data()
    elif year == 2022:
        return read_cattle_data()
    else:
        raise HTTPException(status_code=404, detail=f"Year {year} not found.")


@router.put(
    "/{total_year}}",
    tags=["cattle"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return dict(total_cattle=get_total_cattle_by_year)
