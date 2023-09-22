from . import plans, sample
from fastapi import APIRouter

router = APIRouter()
#router.include_router(users.router, prefix="/users")
router.include_router(plans.router, prefix="/plans")
router.include_router(sample.router, prefix="/sample")