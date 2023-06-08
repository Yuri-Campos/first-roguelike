from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console


from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

# Engine class, used to handle the tcod events (more stuff to be implemented)
class Engine:
    ''' 
    Constructor of the class contains a set of entities (created on the main for now), an event_handler 
    object of the subclass EventHandler, child of the tcod EventDispatch, and a player entity 
    '''
    def __init__(self, entities: Set[Entity], event_handler:EventHandler, game_map: GameMap, player: Entity):
        self.entities = entities
        self.game_map = game_map
        self.event_handler = event_handler
        self.player = player

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

    '''
    This is our render. He takes the tcod console and context created on the main funtcion and render 
    all the entities on it.
    '''        
    def render(self, console: Console, context: Context) -> None:

        self.game_map.render(console)
        # getting all the entities in the class iterable and printing them on the console
        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg = entity.color)

        # presenting the console with the entities
        context.present(console)

        # clearing the console (This will allow us to refresh the entity parametres like it's position)
        console.clear()    