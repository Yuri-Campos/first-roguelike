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
        ('walkable', np.bool),
        ('transparent', np.bool),
        ('dark', graphic_data_tiles),
    ]
)

def new_tile(
        *,
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int ], Tuple[int, int, int]]
) -> np.ndarray:
    return np.array((walkable, transparent, dark), dtype = tile_data)

floor = new_tile(
    walkable=True, transparent=True, dark=(ord(' '), (255,255,255), (50, 50, 150)),
)

wall = new_tile(
    walkable=False, transparent=False, dark=(ord(' '), (255, 255, 255)(0, 0, 100)),
)