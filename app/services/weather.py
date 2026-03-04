from fastapi import HTTPException

from app.schemas.weather import WeatherResponse, WeatherRequest, WeatherData
from app.services.cache import CacheService
from app.core.config import settings
from app.core.http_client import client
import urllib.parse

class WeatherService:
    def __init__(self, cache: CacheService):
        self.cache = cache

    async def get_weather(self, request: WeatherRequest) -> WeatherResponse:
        safe_location=urllib.parse.quote(request.location)
        cache_key = f"weather:{safe_location}:{request.date1}:{request.date2}"
        
        cached = await self.cache.get(cache_key)
        if cached:
            return WeatherResponse.model_validate_json(cached)

        base_url=f"{settings.API_URL}/{request.location}"
        if request.date1 and request.date2:
            url = f"{base_url}/{request.date1}/{request.date2}"
        elif request.date1:
            url = f"{base_url}/{request.date1}"
        elif request.date2:
            raise HTTPException(status_code=400, detail="date1 is required when using date2")
        else:
            url = base_url
        
        try:
                
            response = await client.get(
                url,
                params={
                    "key": settings.API_KEY,
                    "unitGroup": "metric",
                }
            )
            response.raise_for_status() # check response status and automatically throw exception

        except Exception:
            raise HTTPException(status_code=500, detail="Weather provider error")
        
        raw_data = response.json()

        # list for map data
        weather_list = []

        for day in raw_data.get("days", []):
            weather_list.append(
                WeatherData(
                    date_time=day["datetime"],
                    temperature=day["temp"],
                    description=day.get("description", ""),
                    feels_like=day.get("feelslike"),
                    humidity=day["humidity"]
                )
            )

        result = WeatherResponse(
            location=request.location,
            data=weather_list
        )

        await self.cache.set(cache_key, result.model_dump_json(), ttl=settings.CACHE_TTL)

        return result