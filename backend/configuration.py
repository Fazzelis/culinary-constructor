from pydantic_settings import BaseSettings
from typing import ClassVar


class Settings(BaseSettings):
    url: str = "https://26.122.80.20:8000"
    get_attachment_url: str = f"{url}/attachment/get?attachment_id="


settings = Settings()
