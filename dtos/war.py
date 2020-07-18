from datetime import datetime
from dtos.participants import Participants
from pydantic import BaseModel
from typing import List, Optional

class War(BaseModel):
    created_date: datetime
    participants: List[Participants]

    def __repr__(self):
        return '<War {}>'.format(self.created_date.strftime('%d-%m-%Y'))