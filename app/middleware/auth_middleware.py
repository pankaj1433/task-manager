from fastapi import Request, HTTPException
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse

from app.deps import get_db
from app.core.config import settings
from app.schemas.user import TokenData
from app.services.user_service import get_user_by_username

PROTECTED_PATHS = "/internal"


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if PROTECTED_PATHS in request.url.path:
            if "authorization" not in request.headers:
                return JSONResponse(
                    status_code=403, content={"detail": "Not authenticated"}
                )
            auth_header = request.headers["authorization"]
            try:
                scheme, token = auth_header.split()
                if scheme.lower() != "bearer":
                    raise HTTPException(
                        status_code=403, detail="Invalid authentication scheme"
                    )
                payload = jwt.decode(
                    token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
                )
                username: str = payload.get("sub")
                if username is None:
                    raise HTTPException(status_code=403, detail="Invalid token")
                token_data = TokenData(username=username)
            except JWTError:
                raise HTTPException(status_code=403, detail="Invalid token")
            db: Session = next(get_db())
            user = get_user_by_username(db, username=token_data.username)
            if user is None:
                raise HTTPException(status_code=403, detail="User not found")
            # if not user.is_active:
            #     raise HTTPException(status_code=403, detail="Inactive user")
            request.state.user = user

        response = await call_next(request)
        return response
