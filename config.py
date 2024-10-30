import os
from typing import List

from dotenv import load_dotenv

load_dotenv()

ENV: str = ""


class Configs:
    # BASE
    env: str = os.getenv("ENV", "dev")
    api: str = "/api"
    prefix: str = "/api/v1"
    project_name: str = "BoilerPlate"

    # DATE
    datetime_format: str = "%Y-%m-%dT%H:%M:%S"
    date_format: str = "%Y-%m-%d"

    project_root: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # AUTH
    secret_key: str = os.getenv("SECRET_KEY")
    access_token_expire: int = 60 * 24 * 30  # 60 minutes * 24 hours * 30 days = 30 days

    # CORS
    backend_cors_origins: List[str] = ["*"]

    # DATABASE
    engine: str = os.getenv("ENGINE")
    user: str = os.getenv("POSTGRES_USER")
    password: str = os.getenv("POSTGRES_PASSWORD")
    database_name: str = os.getenv("POSTGRES_DB")
    host: str = os.getenv("POSTGRES_HOST")
    port: str = os.getenv("POSTGRES_PORT")
    database_url: str = f"{engine}://{user}:{password}@{host}:{port}/{database_name}"



class TestConfigs(Configs):
    ENV: str = "test"


configs = Configs()