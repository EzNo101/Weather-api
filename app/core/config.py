from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    REDIS_URL: str = "redis://localhost:6379"
    API_KEY: str
    API_URL: str

    CACHE_TTL: int
    
    class Config:
        env_file = ".env"

settings = Settings()