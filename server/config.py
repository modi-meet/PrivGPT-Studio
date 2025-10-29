import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    CORS_HEADERS = "Content-Type"
    #here the second value shows the default value if the environment variable is not set
    MONGO_URI = os.getenv("MONGODB_URL", "mongodb://localhost:27017/PrivGPT-Studio")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "your_gemini_api_key")
