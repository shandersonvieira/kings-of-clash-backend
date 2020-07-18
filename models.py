from pydantic import BaseModel
from typing import List
from dtos.war import War


class ResponseModel(BaseModel):
    data: List[War]