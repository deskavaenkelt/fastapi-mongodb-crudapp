from fastapi import APIRouter

hello_router = APIRouter()


@hello_router.get('/')
async def hello():
    return "Welcome to FastAPI"
