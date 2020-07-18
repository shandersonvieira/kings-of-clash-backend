from pydantic import BaseModel

class Participants(BaseModel):
    tag: str
    name: str
    cardsEarned: int
    battlesPlayed: int
    wins: int
    collectionDayBattlesPlayed: int
    numberOfBattles: int