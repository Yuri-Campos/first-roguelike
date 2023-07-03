from entity import Entity

player = Entity(char='@', color=(255,255,255), name='Player', blocks_movement=True)

infantry = Entity(char='i', color=(204, 0, 0), name='Imperial Infantryman', blocks_movement=True)
machineman = Entity(char='M', color=(255, 51, 51), name='MachineMan', blocks_movement=True)