from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import User, UserCreate
from app.database import SessionLocal, engine

router = APIRouter()


@router.post("/", response_model=User)
def create_user(user: UserCreate):
  return {"Message": "Post for create user"}