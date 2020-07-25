from datetime import datetime

from dotenv import load_dotenv
from dotenv_settings_handler import BaseSettingsHandler

load_dotenv()

class Settings(BaseSettingsHandler):
    CLASH_URL: str
    CLAN_TAG: str
    API_KEY: str
    SSL_VERIFY: bool
    API_CLASH_LIMIT: int
    WAR_START_DATE: datetime
    WAR_END_DATE: datetime
    ZERO_VICTORY: int
    ONE_VICTORY: int
    TWO_VICTORY: int
    TREE_VICTORY: int

settings = Settings()