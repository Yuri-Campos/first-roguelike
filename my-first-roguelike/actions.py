# main class, it will be filled with stuff in the future
class Action:
    pass

# EscapeAction will be implemented in the future
class EscapeAction():
    pass

# Subclass of the Action class, used to modify the postition of an entity
class MovementAction():
    def __init__(self, dx: int, dy: int) -> None:
        super().__init__()

        self.dx = dx
        self.dy = dy
