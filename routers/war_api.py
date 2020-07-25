from fastapi import APIRouter
from fastapi_utils.inferring_router import InferringRouter
from settings import settings

from services.war_service import WarService
from services.tournament_service import TournamentService
from clan_store import ClanStore
from war_store import WarLogStore
from models import TournamentDetailModel
from dtos.tournament_participant import TournamentParticipant
from dtos.tournament import Tournament

router = InferringRouter()


class WarListApiView:

    @router.get('/wars', status_code=200)
    async def get():
        wars = WarLogStore().filter_by_date(
            settings.WAR_START_DATE,
            settings.WAR_END_DATE
        )

        war_resume = []

        clan = ClanStore().get_clan()
        championship_tournament = Tournament()

        for war in wars:
            tournament = Tournament(war=war)
            tournament_service = TournamentService(war, clan)
            championship_tournament.total_wars += 1

            for participant in war.participants:
                tournament_participant = tournament_service.get_tournament_participant(participant)
                tournament.add_participant(tournament_participant)

            championship_tournament.sum(tournament)

        return championship_tournament.dict(
            include={
                'total_wars': ...,
                'participants': {
                    '__all__': {
                        'participant': {'name', 'tag'},
                        'collections': ...,
                        'wars_participated': ...,
                        'matches': ...,
                        'wins': ...,
                        'defeats': ...,
                        'bonus': ...,
                        'punishment': ...,
                        'penalties': ...,
                        'total': ...
                    }
                }
            })