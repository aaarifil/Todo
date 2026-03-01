from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI ToDo"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str = "sqlite:///./dev.db"

    # Auth
    SECRET_KEY: str = "CHANGE_ME"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    class Config:
        env_prefix = ""
        env_file = ".env"
