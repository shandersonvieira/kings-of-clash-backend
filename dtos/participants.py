from pydantic import BaseModel

class Participant(BaseModel):
    tag: str
    name: str
    cards_earned: int
    battles_played: int
    wins: int
    collection_day_battles_played: int
    number_of_battles: int

    def __repr__(self):
        return '<Participant {} - {}>'.format(self.tag, self.name)