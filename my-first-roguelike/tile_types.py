from typing import Tuple

import numpy as np

graphic_data_tiles = np.dtype(
    [
        ('ch', np.int32),
        ('fg', '3B'),
        ('bg', '3B'),
    ]
)

tile_data = np.dtype(
    [
        ('walkable', bool),
        ('transparent', bool),
        ('dark', graphic_data_tiles),
        ('light', graphic_data_tiles),
    ]
)

def new_tile(
        *,
        walkable: bool,
        transparent: bool,
        dark: Tuple[int, Tuple[int, int, int ], Tuple[int, int, int]],
        light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    return np.array((walkable, transparent, dark, light), dtype = tile_data)


SHROUD = np.array((ord(' '), (255,255,255), (0,0,0)), dtype=graphic_data_tiles)

floor = new_tile(
    walkable=True, 
    transparent=True, 
    dark=(ord(' '), (255,255,255), (50, 50, 150)),
    light=(ord(' '), (255, 255, 255), (200,180,50)),
)

wall = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord(' '), (255, 255, 255), (0, 0, 100)),
    light=(ord(' '), (255, 255, 255), (130, 110, 50)),
)