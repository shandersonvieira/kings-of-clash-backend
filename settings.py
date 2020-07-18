from dotenv import load_dotenv
from dotenv_settings_handler import BaseSettingsHandler

load_dotenv()

class Settings(BaseSettingsHandler):
    CLASH_URL: str
    CLAN_TAG: str
    API_KEY: str
    SSL_VERIFY: bool
    API_CLASH_LIMIT: int

settings = Settings()