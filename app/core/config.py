from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    project_name: str = "SentinelIQ"
    project_version: str = "0.1.0"

    class Config:
        env_file = ".env"

settings = Settings()

