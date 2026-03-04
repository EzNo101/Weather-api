from fastapi import Depends
from redis.asyncio import Redis

from app.core.redis import redis_client
from app.services.weather import WeatherService
from app.services.cache import CacheService
from app.services.rate_limiter import RateLimiterService

def get_redis() -> Redis:
    return redis_client

def get_cache_service(redis: Redis = Depends(get_redis)) -> CacheService:
    return CacheService(redis)

def get_weather_service(cache: CacheService = Depends(get_cache_service)) -> WeatherService:
    return WeatherService(cache)

def get_rate_limiter_service(redis: Redis = Depends(get_redis)) -> RateLimiterService:
    return RateLimiterService(redis)