import os
from services.weather_api import get_weather
from logger import logger
from dotenv import load_dotenv

logger.info("App started")

load_dotenv()

api_key = os.environ.get("API_KEY")
if not api_key:
    raise RuntimeError("API_KEY is missing,. Set it in .env")

city = input("Enter city name: ")

weather = get_weather(city, api_key)

if "error" in weather:
    logger.error("API error : %s", weather["error"])
else:
    logger.info("Fetching weather for %s", weather["location"])
    logger.info("Temperature: %s °C", weather["temp_c"])
    logger.info("Condition: %s", weather["condition"])
    logger.info("Weather data fetched successfully.")
