from fastapi import APIRouter, Depends
from app.dependencies import get_query_token

router = APIRouter(
    prefix="/new",
    tags=["new"],
    dependencies=[Depends(get_query_token)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def new_endpoint():
    return {"message": "This is a new endpoint!"}