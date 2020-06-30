import sys
from settings import Settings
from ship import Ship
import pygame

# Overall class to manage game assets and behavior, cont on page 238
class alienInvasion:

    # init function to run upon launch
    def __init__(self):
        # initialize the game and game creation resources
        pygame.init()

        # window, import settings from settings.py script
        self.settings = Settings()

        # apply window dimensions
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        # set title of window
        pygame.display.set_caption("Alien Invasion")

        # init ship
        self.ship = Ship(self)

        # set background color
        self.bg_color = (0, 0, 255)
    
    def runGame(self):

        # start main game loop
        while True:

            # check for input events while loop
            self._check_events()
            
            # update screen while looping
            self._update_screen()
    
    # function to check for keypresses and mouse events
    def _check_events(self):

            # watch for keyboard and mouse events for exit window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    # function to update screen in loop
    def _update_screen(self):

            # redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            # position ship
            self.ship.blitme()
            
            # make the most recent drawn screen visible
            pygame.display.flip()

# run class and game
if __name__ == '__main__':

    # make a game instance and run the game
    ai = alienInvasion()
    ai.runGame()
