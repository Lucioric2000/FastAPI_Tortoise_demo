from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0