from fastapi import APIRouter
from app.routes import user
from app.core.config import settings

router = APIRouter()
router.include_router(
    user.router, prefix=f"{settings.API_V1_STR}/users", tags=["users"]
)
