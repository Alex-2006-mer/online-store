from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    DATABASE_URL: str = Field(..., alias="DATABASE_URL")
    catalog_service_url: str = "http://catalog-service:8000"
    http_timeout_seconds: float = 5.0

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_ignore_empty=True,
    )



settings = Settings()


class NotFoundError(Exception):
    pass