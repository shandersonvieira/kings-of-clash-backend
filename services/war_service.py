import requests
import os
from fastapi import HTTPException
from urllib.parse import quote

from settings import settings


class WarService:

    def get_header(self) -> dict:
        return {
            'authorization': 'Bearer {}'.format(settings.API_KEY)
        }

    def get_war_url(self) -> str:
        return os.path.join(settings.CLASH_URL, 'v1', 'clans', quote(settings.CLAN_TAG), 'warlog')

    def get_war_log(self) -> dict:
        resp = requests.get(self.get_war_url(),
                            verify=settings.SSL_VERIFY,
                            params={'limit': settings.API_CLASH_LIMIT},
                            headers=self.get_header())

        if not resp.ok:
            raise HTTPException(status_code=404, detail="Item not found")

        return resp.json()