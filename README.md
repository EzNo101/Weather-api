
# Weather API Task

This is a modern async weather API built with FastAPI, designed to fetch and return weather data from the Visual Crossing Weather API. The project demonstrates best practices for working with 3rd party APIs, Redis caching, environment variables, and rate limiting in Python.

## Features
- Fetches weather data for a given location and date(s) from Visual Crossing
- Asynchronous, production-ready codebase
- In-memory caching with Redis (configurable TTL)
- Rate limiting per client (IP) using Redis
- Clean, layered project structure (schemas, services, core, API)
- Environment variables for all secrets/configuration
- Error handling for invalid requests and provider issues

## Tech Stack
- Python 3.12+
- FastAPI
- Redis (async, via redis-py)
- httpx (async HTTP client)
- Pydantic v2 (data validation)
- uv (for dependency management)

## Quickstart
1. **Clone the repository**
2. **Install dependencies** (using [uv](https://github.com/astral-sh/uv))
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install -r pyproject.toml
   ```
   Or simply:
   ```bash
   uv pip install -r pyproject.toml
   ```
3. **Configure environment variables**
   - Copy `.env.example` to `.env` (or create `.env` manually):
     ```env
     REDIS_URL=redis://localhost:6379
     CACHE_TTL=43200
     API_KEY=your_visualcrossing_api_key
     API_URL=https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline
     ```
   - Adjust values as needed.
4. **Run Redis server** (locally or use a cloud provider)
5. **Start the API server**
   ```bash
   uvicorn app.main:app --reload
   ```
6. **Explore the API**
   - Interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## Example Request
```
GET /weather/date1/date2?API_KEY
```

## Project Structure
```
app/
  main.py           # FastAPI app entrypoint
  api/              # API routers
  schemas/          # Pydantic models
  services/         # Business logic, cache, rate limiter
  core/             # Config, Redis, dependencies
pyproject.toml      # Project metadata & dependencies
uv.lock             # uv dependency lockfile
.env                # Environment variables
```

## About
This project was created by me as a practical task from [roadmap.sh](https://roadmap.sh/projects/weather-api-wrapper-service) to practice working with 3rd party APIs, async Python, Redis caching, and rate limiting in FastAPI.

---

Feel free to use or modify this project for your own learning!
