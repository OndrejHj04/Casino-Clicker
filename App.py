import pygame
import time
from index import casino_money
from button_class import Button
class PygameApp:
    def __init__(self):
        pygame.init()
        self.casino = casino_money()
        self.size = pygame.display.get_desktop_sizes()
        self.screen = pygame.display.set_mode((self.size[0][0], self.size[0][1] - 55), pygame.RESIZABLE)
        pygame.display.set_caption("Pygame Button Demo")
        self.button = Button(200, 200, 200, 50, self.casino)
        self.sekunda_interval = 1
        self.cas_posdniho_pridani = time.time()
        self.penize = 0

    def run(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                self.button.handle_event(event)

            aktualni_cas = time.time()
            if aktualni_cas - self.cas_posdniho_pridani >= self.sekunda_interval:
                self.penize = self.penize + self.casino.value_x()
                print(self.penize)
                self.cas_posdniho_pridani = aktualni_cas

            self.screen.fill((255, 255, 255))  # White background
            self.button.draw(self.screen)

            pygame.display.flip()

            clock.tick(60)  # Cap the frame rate at 60 frames per second

if __name__ == "__main__":
    app = PygameApp()
    app.run()