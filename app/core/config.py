from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Task Manager App"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str
    SECRET_KEY: str = "dev-mode-secret"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
