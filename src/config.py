from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    ACCESS_TOKEN_EXPIRY: int
    REFRESH_TOKEN_EXPIRY: int
    JWT_ALGORITHM: str
    JWT_SECRET: str

    model_config = SettingsConfigDict(
        env_file="src/.env",
        extra="ignore"
    )

Config = Settings()

