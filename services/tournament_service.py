from dtos.tournament_participant import TournamentParticipant
from fastapi import HTTPException
from settings import settings

class TournamentService:
    def __init__(self, war, clan):
        self.war = war
        self.clan = clan

    def get_tournament_arena(self):
        return self.clan.get_arena_score_table()

    def get_participant_collections(self, participant):
        arena = self.get_tournament_arena()

        # < 840
        if participant.cards_earned <= arena.default:
            return participant.cards_earned

        # >= 840 < 900
        elif participant.cards_earned >= arena.default and participant.cards_earned <= arena.zero_victory:
            return settings.ZERO_VICTORY

        # > 900 < 1200
        elif participant.cards_earned > arena.zero_victory and participant.cards_earned < arena.one_victory:
            return settings.ONE_VICTORY

        # > 1200 < 1500
        elif participant.cards_earned > arena.one_victory and participant.cards_earned <= arena.two_victory:
            return settings.TWO_VICTORY

        # > 1500
        elif participant.cards_earned > arena.two_victory:
            return settings.TREE_VICTORY

        else:
            raise HTTPException(status_code=400, detail='Pontuação não encontrada')

    def get_tournament_participant(self, participant):
        tournament_participant = TournamentParticipant(
            participant=participant,
            collections=self.get_participant_collections(participant),
            wins=participant.wins
        )

        return tournament_participant
