from fastapi import APIRouter
from app.models.user_model import User
from typing import List


router = APIRouter()

fake_users_db = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]

@router.get("/users", response_model=List[User])
async def get_users():
    return fake_users_db
