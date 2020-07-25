from pydantic import BaseModel
from fastapi import HTTPException
from arenas import GoldArena, LegendaryArena

class Clan(BaseModel):
    tag: str
    clan_war_trophies: int

    def __repr__(self):
        return '<Clan {}>'.format(self.tag)

    def get_arena_score_table(self):
        if self.clan_war_trophies < 3000:
            return GoldArena()
        elif self.clan_war_trophies > 3000:
            return LegendaryArena()

        raise HTTPException