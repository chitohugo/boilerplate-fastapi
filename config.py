import os
from typing import List

from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """Base configuration settings."""
    env: str = os.getenv("ENV", "dev")
    api: str = "/api"
    prefix: str = "/api/v1"
    project_name: str = "BoilerPlate"

    datetime_format: str = "%Y-%m-%dT%H:%M:%S"
    date_format: str = "%Y-%m-%d"

    project_root: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # AUTH
    secret_key: str = os.getenv("SECRET_KEY")
    access_token_expire: int = 60 * 24 * 30  # 60 minutes * 24 hours * 30 days = 30 days

    backend_cors_origins: List[str] = ["*"]

    # DATABASE
    engine: str = os.getenv("ENGINE")
    user: str = os.getenv("POSTGRES_USER")
    password: str = os.getenv("POSTGRES_PASSWORD")
    database_name: str = os.getenv("POSTGRES_DB")
    host: str = os.getenv("POSTGRES_HOST")
    port: str = os.getenv("POSTGRES_PORT")
    database_url: str = f"{engine}://{user}:{password}@{host}:{port}/{database_name}"


class TestConfig(BaseConfig):
    """Test configuration settings."""
    env: str = "test"
    sqlite_file_name = "character.db"
    database_url: str = f"sqlite:///{sqlite_file_name}"


def get_settings() -> BaseConfig:
    env = os.getenv("ENV", "dev")
    if env == "test":
        return TestConfig()
    return BaseConfig()


settings = get_settings()
