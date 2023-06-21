from __future__ import annotations

import copy
from typing import Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from game_map import GameMap
  
T = TypeVar('T', bound='Entity')


'''
This is the Entity class, its pretty simple now but later we will add more stuff.
This class will represent most of the things in our game like the player, NPCs, Enemies, items, etc.
For now the only method of the class is the move(), responsible for refreshing the entity coordinates
'''
class Entity:
    '''The class constructor recieves the entity X & Y coordinates,
      the char that represents it and a tuple with the three integers 
      representing the RGB color of the entity.'''
    def __init__(self, x: int = 0, 
                 y: int = 0, 
                 char: str = '?', 
                 color: Tuple[int, int, int] = (255,255,255),
                 name: str = '<Unnamed>',
                 blocks_movement: bool = False):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement
      
    def spawn(self: T, gamemap: GameMap, x: int, y: int)-> T:
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        gamemap.entities.add(clone)
        return clone

    # The move() method takes the "size" of the movement in the x and y coordinates and apply it to the entity coordinates
    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy