import pygame


class Label:
    def __init__(self, font_size, color, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, font_size)
        self.color = color
        self.position = (x, y)
        self.text = ""

    def update_text(self, new_text):
        self.text = new_text

    def render(self, screen):
        pygame.draw.rect(screen, "blue", self.rect)
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(topleft=self.position)
        screen.blit(text_surface, text_rect)
