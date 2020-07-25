import requests
import os
from fastapi import HTTPException
from urllib.parse import quote

from settings import settings
from . import Service


class ClanService(Service):

    def get_clan_url(self) -> str:
        return os.path.join(settings.CLASH_URL, 'v1', 'clans', quote(settings.CLAN_TAG))

    def get_clan(self) -> dict:
        resp = requests.get(self.get_clan_url(),
                            verify=settings.SSL_VERIFY,
                            headers=self.get_header())

        if not resp.ok:
            raise HTTPException(status_code=404, detail="Item not found")

        return resp.json()