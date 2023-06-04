import tcod

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


if __name__ == '__main__':
    main()
