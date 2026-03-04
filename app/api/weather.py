from fastapi import APIRouter, Depends, Request

from app.core.dependencies import get_rate_limiter_service, get_weather_service
from app.schemas.weather import WeatherResponse, WeatherRequest
from app.services.weather import WeatherService
from app.services.rate_limiter import RateLimiterService 

router = APIRouter(prefix="/weathers", tags=["weather"])

@router.post("/", response_model=WeatherResponse)
async def get_weather(
    request_data: WeatherRequest,
    request: Request,
    weather_service: WeatherService = Depends(get_weather_service),
    rate_limiter_service: RateLimiterService = Depends(get_rate_limiter_service)
):
    client_ip = request.client.host

    await rate_limiter_service.check(client_ip)

    return await weather_service.get_weather(request_data)