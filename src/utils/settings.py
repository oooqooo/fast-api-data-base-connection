from pydantic_settings import BaseSettings,SettingsConfigDict
import sqlalchemy

class Settings(BaseSettings):
    db_connection: str
    model_config = SettingsConfigDict(env_file=".env",extra="ignore")
settings = Settings()