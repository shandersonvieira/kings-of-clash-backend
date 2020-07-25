from pydantic import BaseModel
from .participants import Participant

class TournamentParticipant(BaseModel):
    participant: Participant = None
    collections: int = 0
    wars_participated: int = 1
    matches: int = 1
    wins: int = 0
    defeats: int = 0
    bonus: int = 0
    punishment: int = 0
    penalties: int = 0
    total: int = 0

    def __repr__(self):
        return '<TournamentParticipant {}>'.format(self.participant.name if self.participant else None)