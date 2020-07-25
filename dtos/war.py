from datetime import datetime
from dtos.participants import Participant
from pydantic import BaseModel
from typing import List

class War(BaseModel):
    war_date: datetime
    participants: List[Participant]

    def __repr__(self):
        return '<War {}>'.format(self.war_date.strftime('%d-%m-%Y'))