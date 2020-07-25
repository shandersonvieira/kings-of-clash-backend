from fastapi import HTTPException
from dateutil.parser import isoparse
from datetime import datetime
from typing import List

from services.war_service import WarService
from dtos.participants import Participant
from dtos.war import War


class WarLogStore:
    war_service = WarService()

    def get(self) -> List[War]:
        resp = self.war_service.get_war_log()

        if not resp['items']:
            raise HTTPException(status_code=404, detail='Api não acessível')

        result = [War(
            war_date=isoparse(war_item['createdDate']),
            participants=[Participant(
                tag=participant['tag'],
                name=participant['name'],
                cards_earned=participant['cardsEarned'],
                battles_played=participant['battlesPlayed'],
                wins=participant['wins'],
                collection_day_battles_played=participant['collectionDayBattlesPlayed'],
                number_of_battles=participant['numberOfBattles']
            ) for participant in war_item['participants']]
        ) for war_item in resp['items']]

        return result

    def filter_by_date(self, war_date_gte: datetime, war_date_lte: datetime) -> List[War]:
        result = self.get()

        for item in list(result):
            if not (self.gte(item, war_date_gte) and self.lte(item, war_date_lte)):
                result.remove(item)

        return result

    def gte(self, item: War, war_date: datetime) -> bool:
        return item.war_date >= war_date

    def lte(self, item: War, war_date: datetime) -> bool:
        return item.war_date <= war_date
