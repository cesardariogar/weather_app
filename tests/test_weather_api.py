from services.weather_api import get_weather
import requests
from unittest.mock import patch


@patch("services.weather_api.requests.get")
def test_get_weather_success(mock_get):
    # @Mock response JSON
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "location": {"name": "London"},
        "current": {"temp_c": 22, "condition": {"text": "Cloudy"}},
    }

    result = get_weather("London", "fake_api")
    assert result == {
        "location": "London",
        "temp_c": 22,
        "condition": "Cloudy",
    }
