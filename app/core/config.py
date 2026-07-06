from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_Name: str = "Wine API"
    APP_Version: str = "1.0.0"
    DATABASE_URL = "sqlite:///wine.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )

settings = Settings()