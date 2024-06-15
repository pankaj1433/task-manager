from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Task Manager App"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = ""

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
