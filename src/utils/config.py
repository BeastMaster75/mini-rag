from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

def get_settings():
    return Settings()