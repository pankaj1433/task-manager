from fastapi import FastAPI
from app.core.config import settings
from app.routes import router
from app.models import user
from app.database import engine
from app.middleware.auth_middleware import AuthMiddleware


def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME)

    # bind models
    user.Base.metadata.create_all(bind=engine)

    # configure middlewares
    app.add_middleware(AuthMiddleware)

    # configure routes
    app.include_router(router)

    return app
