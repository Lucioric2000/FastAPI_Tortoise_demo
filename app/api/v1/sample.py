from fastapi import APIRouter
from ...db.models import sample
from starlette.exceptions import HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
import logging

logger = logging.getLogger(__name__)
router = APIRouter()
# Update User Profile


@router.get("/")
async def list_users():
    return await sample.Test_table_Pydantic.from_queryset(sample.Test_table.all())


@router.post("/")
async def create_user(user: sample.Test_table_Pydantic):
    userobj = await sample.Test_table.create(**user.dict())
    return await sample.Test_table_Pydantic.from_tortoise_orm(userobj)


@router.get("/{userid:int}/")
async def get_user(userid: int):
    return await sample.Test_table_Pydantic.from_queryset_single(sample.Test_table.get(id=userid))


@router.delete("/{userid:int}/")
async def delete_user(userid: int):
    deleted_count = await sample.Test_table.filter(id=userid).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {userid} not found")
    return {"message": f"Deleted user {userid}"}


@router.put("/{userid:int}/", response_model=sample.Test_table_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def update_user(userid: int, user: sample.Test_table_in_Pydantic):
    await sample.Test_table.filter(id=userid).update(**user.dict(exclude_unset=True))
    return await sample.Test_table_Pydantic.from_queryset_single(sample.Test_table.get(id=userid))