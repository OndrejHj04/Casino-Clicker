import pygame
from index import casino_money


class Button:
    def __init__(self, x, y, width, height, obj_casino, text, color=(200, 0, 0), highlight_color=(255, 255, 255), font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.obj_casino = obj_casino
        self.text = text
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

    def handle_event(self, newEvent, event):
        newEvent(self, event)
