from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.schemas.user import User, UserCreate
from app.deps import get_db
from app.services.user_service import (
    create_user as create_user_service,
    get_user_by_email,
    get_user_by_username,
)

public_router = APIRouter(prefix="/users")
internal_router = APIRouter(prefix="/internal/users")


@public_router.post("", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered!")
    return create_user_service(db, user)


@internal_router.get("/current", response_model=User)
def get_current_user_details(request: Request, db: Session = Depends(get_db)):
    user = request.state.user
    db_user = get_user_by_username(db, user.username)
    # if None in db_user:
    #     raise HTTPException(status_code=403, detail="User not found")
    return db_user
