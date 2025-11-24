from pydantic_settings import BaseSettings
from typing import ClassVar


class Settings(BaseSettings):
    # url: str = "http://26.122.80.20:8000"
    url: str = "http://127.0.0.1:8000"
    get_attachment_url: str = f"{url}/attachment?attachment_id="


settings = Settings()
