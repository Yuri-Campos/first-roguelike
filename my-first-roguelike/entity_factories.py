from entity import Entity

player = Entity(char='@', color=(255,255,255), name='Player', blocks_movement=True)

infantry = Entity(char='i', color=(186, 159, 164), name='Imperial Infantry', blocks_movement=True)
machineman = Entity(char='M', color=(205, 35, 64), name='MachineMan', blocks_movement=True)