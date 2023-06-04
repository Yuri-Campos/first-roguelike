import tcod
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main():
    # Variables that hold the size of our tcod screen
    screen_width = 80 # this will be read from a JSON file in the future
    screen_height = 50 # same

    # Player position
    # Will be the middle of the screen for now
    player_x = int(screen_width/2) 
    player_y = int(screen_width/2)

    # Reading and Storing the tileset
    tileset = tcod.load_tilesheet('tileset.png', 32, 8, tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title='My First Roguelike',
        vsync=True,
    )as context:
        root_console = tcod.console(screen_width,screen_height, order='F')

if __name__ == '__main__':
    main()
