from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    PROJECT_NAME: str

    DATABASE_URL: str

    DEBUG: bool = False

    ENVIRONMENT: str = "development"

    LOG_LEVEL: str = "INFO"

    API_KEY_HEADER: str = "X-API-Key"

    CORS_ORIGINS: str = "http://localhost:3000"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()