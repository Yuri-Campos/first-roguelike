from __future__ import annotations

from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class Action(ABC):
    @abstractmethod
    def perform(self, engine: Engine, entity: Entity) -> None:
        ...

class ActionWithDirection(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy

    def perform(self, Engine: Engine, entity: Entity) -> None:
        raise NotImplementedError()
# EscapeAction will be implemented in the future
class EscapeAction(Action):
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()


class MeleeAction(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
       dest_x = entity.x + self.dx
       dest_y = entity.y + self.dy
       target = engine.game_map.get_blocking_entity_at_location(dest_x, dest_y)
       if not target:
           return
       print(f'You kick the {target.name}, much to its annoyance!')

# Subclass of the Action class, used to modify the postition of an entity
class MovementAction(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
        destiny_x = entity.x + self.dx
        destiny_y = entity.y + self.dy

        if not engine.game_map.in_bounds(destiny_x, destiny_y):
            return # Destination is out of bounds.
        if not engine.game_map.tiles['walkable'][destiny_x, destiny_y]:
            return # Destination is blocked by a tile.
        if engine.game_map.get_blocking_entity_at_location(destiny_x,destiny_y):
            return           
        entity.move(self.dx, self.dy)

class BumpAction(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return MeleeAction(self.dx, self.dy).perform(engine, entity)
        else:
            return MovementAction(self.dx, self.dy).perform(engine, entity)