import requests
import time
import logging



def get_weather(city, api_key):
    url = f"https://api.weatherapi.com/v1/current.json?q={city}&key={api_key}"
    start = time.time()
    response = requests.get(url, timeout=5)
    print("Took", round(time.time() - start, 2), "seconds")

    if response.status_code != 200:
        return {"error": response.text}

    data = response.json()
    return {
        "location": data["location"]["name"],
        "temp_c": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"],
    }


"""
Mock version for testing purposes
def get_weather(city, api_key):
    return {"location": city.title(), "temp_c": 25, "condition": "Mock Sunny"}
"""
