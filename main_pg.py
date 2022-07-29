import pygame
import sys
from main import Game



SIZE = (1280, 720)

MAX_TPS = 70.0


class GamePy():
    def __init__(self):
        # Config
        self.tps_max = MAX_TPS
        self.game = Game()
        self.board = self.game.get_board()

        # Initialisation
        pygame.init()
        self.screen = pygame.display.set_mode(size=SIZE)

        self.tps_clock = pygame.time.Clock()
        self.delta = 0.0

        self.game.pygame_start()

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
            # Ticking
            self.delta += self.tps_clock.tick() / 1000.0
            while self.delta > 1 / self.tps_max:
                self.delta -= 1 / self.tps_max
                self.tick()
            # Drawing
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):
        self.board.tick()

    def draw(self):
        self.board.draw()


if __name__ == "__main__":
    GamePy()