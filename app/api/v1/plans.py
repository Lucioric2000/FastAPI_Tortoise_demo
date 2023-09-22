from fastapi import APIRouter

router = APIRouter()

# List Available Plans
@router.get("/")
async def list_plans():
    # Logic to fetch and display available insurance plans
    return {"message": "Available plans fetched", "plans": ["Plan A", "Plan B", "Plan C"]}

# Choose a Plan
@router.post("/choose/")
async def choose_plan(application_id: str, plan_name: str):
    # Logic to associate a plan with an application
    return {"message": "Plan chosen", "plan_name": plan_name}
