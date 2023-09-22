from fastapi import APIRouter
from db.models import users
router = APIRouter()
# Update User Profile
@router.put("/{username}/")
async def update_user(username: str, user: users.Customer):
    # Logic to update the user information
    return {"message": "User information updated"}