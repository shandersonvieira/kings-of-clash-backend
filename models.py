from pydantic import BaseModel
from typing import List
from dtos.war import War
from dtos.tournament_participant import TournamentParticipant
from dtos.tournament import Tournament

class TournamentDetailModel(BaseModel):
    # wars: List[War]
    participants: List[TournamentParticipant]

class ResponseModel(BaseModel):
    data: TournamentDetailModel