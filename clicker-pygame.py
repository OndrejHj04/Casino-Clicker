import pygame
import time
from index import casino_money

pygame.init()
casino = casino_money()
size = pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode((size[0][0], size[0][1] - 55), pygame.RESIZABLE)
sekunda_interval = 1
cas_posdniho_pridani = time.time()
penize = 0

pygame.display.flip()
mainloop = True

print(1)
m = casino_money 
casino.up_cicle(1)   

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
    aktualni_cas = time.time()
    if aktualni_cas - cas_posdniho_pridani >= sekunda_interval:
        penize = penize + casino.value_x() 
        print(penize)
        cas_posdniho_pridani=aktualni_cas

pygame.quit()
