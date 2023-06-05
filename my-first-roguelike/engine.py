from typing import Set, Iterable, AnyStr

from tcod.context import Context
from tcod.console import Console

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler

class Engine:
    def __init__(self, entities: set[Entity], event_handler:EventHandler, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.player = player
