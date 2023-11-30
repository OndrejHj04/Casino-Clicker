import index
import pygame

pygame.init()
size = pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode((size[0][0], size[0][1] - 55), pygame.RESIZABLE)
font = pygame.font.SysFont("arial", 36)
text = font.render(index.casino_money.value_money(), True, (0, 0, 0))
text_rect = text.get_rect(center=(size[0][0] // 2, (size[0][1] - 55) // 2))
¨


pygame.display.flip()
mainloop = True

while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False

    screen.fill((255, 255, 255))
    screen.blit(text, text_rect)
    pygame.display.flip()