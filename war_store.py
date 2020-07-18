from fastapi import HTTPException
from dateutil.parser import isoparse
from typing import List

from services.war_service import WarService
from dtos.participants import Participants
from dtos.war import War


class WarLogStore:
    war_service = WarService()

    def get(self) -> List[War]:
        resp = self.war_service.get_war_log()

        if not resp.ok:
            raise HTTPException(status_code=404, detail="Item not found")

        if not resp.json()['items']:
            raise HTTPException(status_code=404, detail="Item not found")

        result = [War(
            created_date=isoparse(war_item['createdDate']),
            participants=[Participants(
                tag=participant['tag'],
                name=participant['name'],
                cardsEarned=participant['cardsEarned'],
                battlesPlayed=participant['battlesPlayed'],
                wins=participant['wins'],
                collectionDayBattlesPlayed=participant['collectionDayBattlesPlayed'],
                numberOfBattles=participant['numberOfBattles']
            ) for participant in war_item['participants']]
        ) for war_item in resp.json()['items']]

        return result
