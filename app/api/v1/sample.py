from fastapi import APIRouter
from ...db.models import sample
router = APIRouter()
# Update User Profile
@router.put("/{userid:int}/")
async def update_user(userid: int, smple: sample.UTest_table):
    # Logic to update the user information
    return {"message": "User information updated"}

@router.get("/")
async def list_users():
    return sample.Test_table.all()

@router.post("/")
async def create_user(user: sample.UTest_table):
    userobj = sample.Test_table.create(**user.dict())
    await userobj
    #return userobj.save()