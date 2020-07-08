import sys

import pygame

class AlienInvasion:
    """ Overall class to manage game assets and behavaior """

    def __init__(self):
        """ initializes game and creates game resources """
        pygame.init()

        # Background Color
        self.bg_color = (230,230,230)

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Alien INVASION!!!')

    def run_game(self):
        """ start main loop of game """
        while True:
            # watch for keyboard / mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw screen during each pass through loop
            self.screen.fill(self.bg_color)

            # make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run game
    AlienInvasion = AlienInvasion()
    AlienInvasion.run_game()