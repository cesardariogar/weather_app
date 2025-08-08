# weather_app
small weather app exercise (Python with FastApi)

# [🚀 Run the app locally]

**Install dependencies**
pip install -r requirements.txt

**Start the FastAPI server**
uvicorn app:app --reload

**Visit in your browser:**
http://127.0.0.1:8000

# [🐳 Run the app with Docker]

**Build the image**
docker build -t weather-app .

**Run the container**
docker run -d -p 8000:8000 --env-file .env weather-app

**Visit in your browser:**
http://127.0.0.1:8000

# [🧪 Run the tests]
**With verbose output**
pytest -v

