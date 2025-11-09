import os
from dotenv import load_dotenv

load_dotenv()  # reads .env file if present

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
