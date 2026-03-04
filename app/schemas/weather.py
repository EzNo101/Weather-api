from pydantic import BaseModel, Field
from datetime import datetime

class WeatherRequest(BaseModel):
    location: str = Field(...)
    date1: str | None = Field(default=None)
    date2: str | None = Field(default=None)

class WeatherData(BaseModel):
    date_time: datetime
    temperature: float
    description: str
    feels_like: float | None
    humidity: float

class WeatherResponse(BaseModel):
    location: str
    data: list[WeatherData] = Field(..., min_length=1)
