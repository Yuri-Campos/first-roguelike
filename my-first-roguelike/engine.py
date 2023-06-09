from typing import Iterable, Any

from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov

from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

# Engine class, used to handle the tcod events (more stuff to be implemented)
class Engine:
    ''' 
    Constructor of the class contains a set of entities (created on the main for now), an event_handler 
    object of the subclass EventHandler, child of the tcod EventDispatch, and a player entity 
    '''
    def __init__(self, event_handler:EventHandler, game_map: GameMap, player: Entity):
        self.game_map = game_map
        self.event_handler = event_handler
        self.player = player
        self.update_fov()

    def handle_enemy_turns(self) -> None:
        for entity in self.game_map.entities - {self.player}:
            print(f'The {entity.name} wonders when it will get to take a real turn')


    ''' 
    The handle_events function will take an Iterable of events and dispatch it to the event_handler.
    The function will take the event and send it to an ev_*, where * is an event type.
    For example, if a user presses a key, dispatch will call the ev_keydown method that we overrode and will
    return an action. (in this case MovementAction or EscapeAction).
    '''
    def handle_events(self, events: Iterable[Any]) -> None:
        
        # Checking all events (key pressed, mouse movement, mouse click, etc.)
        for event in events:
            #calling the disptach method
            action = self.event_handler.dispatch(event)
            #to do
            if action is None:
                continue
            #checking if the action object is an instance of the MovementAction or EscapeAction classes.
            action.perform(self, self.player)
            self.handle_enemy_turns()
            self.update_fov()
    def update_fov(self) -> None:
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles['transparent'],
            (self.player.x, self.player.y),
            radius=8
        )
        self.game_map.explored |= self.game_map.visible
    '''
    This is our render. He takes the tcod console and context created on the main funtcion and render 
    all the entities on it.
    '''        
    def render(self, console: Console, context: Context) -> None:

        self.game_map.render(console)
        
        context.present(console)

        console.clear()
    