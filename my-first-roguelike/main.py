import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from procgen import generate_dungeon

def main() -> None:
    # Variables that hold the size of our tcod screen
    screen_width = 80 # this will be read from a JSON file in the future
    screen_height = 50 # same

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    # Reading and Storing the tileset
    tileset = tcod.tileset.load_tilesheet('tileset.png', 32, 8, tcod.tileset.CHARMAP_TCOD)

    # Instantianting a EnventHandler() object 
    event_handler = EventHandler()
    # Instantiating a NPC and Player entities
    player = Entity(int(screen_width/2), int(screen_height/2), '@', (255,255,255))
    npc = Entity(int(screen_width/2 - 5), int(screen_height/2), '@', (255,255,0))

    game_map = generate_dungeon(max_rooms=max_rooms, 
                                room_min_size=room_min_size, 
                                room_max_size=room_max_size,
                                map_width=map_width,
                                map_height=map_height,
                                player=player)
    # Storing the entities in a set 
    entities = {npc, player}

    # Instantiating a Engine() object and passing the entities set, event_handler object, player entity and map
    engine = Engine(entities=entities,event_handler=event_handler,game_map=game_map, player=player)
    # ("Opening") Creating the context, passing the screen size, the tileset used by the context and the title
    '''
    In this case vsync is set to True but it doesn't matter that much in that case since vsync main function is syncing
    the terminal framerate with the monitor refresh rate.
    Since our ASCII game wont have animations or smooth movements the difference caused by the vysnc 
    will be almost imperceptible.
    '''
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title='My First Roguelike',
        vsync=True,
    )as context:
        # Creating the console, the order F indicates to numpy that we want the order [x,y] instead of [y,x]
        root_console = tcod.console.Console(screen_width, screen_height, order='F')

        # Game loop
        while True:
            # Calling the render function to render our entities every frame
            engine.render(console=root_console, context=context)

            # Getting an iterator containing the events (mouse movement, key pressed, etc)
            events = tcod.event.wait()
            
            # Calling the handle_events object to handle the events recieved(dispatching to the right ev_* method)
            engine.handle_events(events)

if __name__ == '__main__':
    main()
