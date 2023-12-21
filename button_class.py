import pygame
from index import casino_money


class Button:
    def __init__(self, x, y, width, height, obj_casino, color=(200, 0, 0), highlight_color=(255, 255, 255), font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.obj_casino = obj_casino
        self.text = "Btn"
        self.color = color
        self.highlight_color = highlight_color
        self.font = pygame.font.Font(None, font_size)
        self.clicked = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.highlight_color if self.is_hovered() else self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered():
                self.clicked = True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.clicked and self.is_hovered():
                self.obj_casino.up_cicle(3)
            self.clicked = False
