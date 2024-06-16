from fastapi import APIRouter
from app.routes import user, auth
from app.core.config import settings

router = APIRouter()
router.include_router(user.public_router, prefix=settings.API_V1_STR, tags=["users"])
router.include_router(user.internal_router, prefix=settings.API_V1_STR, tags=["users"])
router.include_router(auth.router, prefix=settings.API_V1_STR, tags=["auth"])
