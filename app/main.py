from fastapi import Depends, FastAPI
# from typing  import List
from app.dependencies import get_query_token, get_token_header
from app.internal import admin

# from app.routers import items, users

from app.routers import items, users, cattle

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(users.router)

app.include_router(cattle.router)

app.include_router(items.router)

app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
