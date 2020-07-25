from pydantic import BaseModel
from settings import settings

class Arena(BaseModel):
    default: int
    zero_victory: int
    one_victory: int
    two_victory: int
    tree_victory: int

class GoldArena(Arena):
    default: int = 840
    zero_victory: int = 900 # ou 900 baseado na posição do jogador
    one_victory: int = 1200
    two_victory: int = 1500
    tree_victory: int = 1680

class LegendaryArena(Arena):
    default: int = 1000
    zero_victory: int = 1320
    one_victory: int = 1760
    two_victory: int = 2200
    tree_victory: int = 2640