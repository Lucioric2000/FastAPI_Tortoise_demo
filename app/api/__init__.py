from fastapi import APIRouter
from . import v1
from .. import db
router = APIRouter()
router.include_router(v1.router, prefix="/v1")