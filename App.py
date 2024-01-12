import pygame
import time
from index import casino_money
from button_class import Button

def newEvent(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if self.is_hovered():
            self.clicked = True

    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        if self.clicked and self.is_hovered():
            self.obj_casino.up_cicle(3)
        self.clicked = False


# nefunguje, nezna penize pac neni v ty classe
def pressed_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if self.is_hovered():
            self.clicked = True

    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        if self.clicked and self.is_hovered():
            self.penize += self.obj_casino.value_x()
        self.clicked = False

class PygameApp:
    def __init__(self):
        pygame.init()
        self.casino = casino_money()
        self.size = pygame.display.get_desktop_sizes()
        self.screen = pygame.display.set_mode((self.size[0][0], self.size[0][1] - 55), pygame.RESIZABLE)
        pygame.display.set_caption("Pygame Button Demo")
        self.button_passive_income = Button(200, 200, 200, 50, self.casino, "city")
        self.button_chip_pressed = Button(400, 200, 200, 50, self.casino, "chip")
        self.sekunda_interval = 1
        self.cas_posdniho_pridani = time.time()
        self.penize = 0

    def run(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                self.button_passive_income.handle_event(newEvent, event)
                self.button_chip_pressed.handle_event(pressed_event,event)

            aktualni_cas = time.time()
            if aktualni_cas - self.cas_posdniho_pridani >= self.sekunda_interval:
                self.penize = self.penize + self.casino.value_x()
                print(self.penize)
                self.cas_posdniho_pridani = aktualni_cas

            self.screen.fill((255, 255, 255))  # White background
            self.button_passive_income.draw(self.screen)
            self.button_chip_pressed.draw(self.screen)

            pygame.display.flip()

            clock.tick(60)  # Cap the frame rate at 60 frames per second

if __name__ == "__main__":
    app = PygameApp()
    app.run()