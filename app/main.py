from fastapi import FastAPI
from app.core.config import settings
from app.routes import router
from app.models import user
from app.database import engine


def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME)
    user.Base.metadata.create_all(bind=engine)
    app.include_router(router)

    return app
