from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    version: str = "1.0.0"
    debug: bool = True
    database_url: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str
    class Config:
        env_file = ".env"


settings = Settings()