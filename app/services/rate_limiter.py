from fastapi import HTTPException
from redis.asyncio import Redis

class RateLimiterService:
    def __init__(self, redis: Redis):
        self.redis = redis

    async def check(self, ip: str, limit: int = 30, window: int = 60):

        key = f"rate:{ip}"

        current = await self.redis.incr(key)

        if current == 1:
            await self.redis.expire(key, window)

        if current > limit:
            raise HTTPException(status_code=429,detail="Too many requests")

        return True