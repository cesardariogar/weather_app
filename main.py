from fastapi import FastAPI, HTTPException
from services.weather_api import get_weather
import os
from dotenv import load_dotenv
from logger import logger

logger.info("WebApp started")

load_dotenv()

app = FastAPI()
API_KEY = os.getenv("API_KEY")


@app.get("/weather")
def weather(city: str):
    logger.info("Fetching weather for %s", city)
    if not API_KEY:
        logger.error("API_KEY is missing.")
        raise HTTPException(status_code=500, detail="API key not configured.")

    result = get_weather(city, API_KEY)

    if "error" in result:
        logger.error("API error for city %s: %s", city, result["error"])
        raise HTTPException(status_code=400, detail=result["error"])

    logger.info("Weather data fetched successfully for %s", city)
    return result


@app.get("/health")
def health():
    logger.info("Health check called")
    return {"status": "ok"}


@app.get("/logs")
def logs():
    try:
        with open("app.log", "r+") as f:
            return {"log": f.read()[-2000:]}  # At least 2k characters
    except Exception as e:
        logger.error("Error reading logs: %s", str(e))
        raise HTTPException(status_code=500, detail="Could not read logs")
