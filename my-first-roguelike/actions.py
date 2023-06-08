from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

# main class, it will be filled with stuff in the future
class Action:
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise NotImplementedError()

# EscapeAction will be implemented in the future
class EscapeAction(Action):
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()

# Subclass of the Action class, used to modify the postition of an entity
class MovementAction(Action):
    def __init__(self, dx: int, dy: int) -> None:
        super().__init__()

        self.dx = dx
        self.dy = dy

    def perform(self, engine: Engine, entity: Entity) -> None:
        destiny_x = entity.x + self.dx
        destiny_y = entity.y + self.dy

        if not engine.game_map.in_bounds(destiny_x, destiny_y):
            return # Destination is out of bounds.
        if not engine.game_map.tiles['walkable'][destiny_x, destiny_y]:
            return # Destination is blocked by a tile.
            
        entity.move(self.dx, self.dy)

