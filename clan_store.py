from fastapi import HTTPException
from services.clan_service import ClanService
from dtos.clan import Clan
from typing import List


class ClanStore:
    clan_service = ClanService()

    def get_clan(self) -> List[Clan]:
        resp = self.clan_service.get_clan()

        if not resp:
            raise HTTPException(status_code=404, detail="Item not found")

        clan = Clan(
            tag=resp['tag'],
            clan_war_trophies=resp['clanWarTrophies']
        )

        return clan
