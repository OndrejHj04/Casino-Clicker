import pygame

pygame.init()
size = pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode((size[0][0], size[0][1] - 55), pygame.RESIZABLE)

pygame.display.flip()
mainloop = True

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
