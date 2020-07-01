import sys
from settings import Settings
from ship import Ship
import pygame

# Overall class to manage game assets and behavior, cont on page 247
class alienInvasion:

    # init function to run upon launch
    def __init__(self):

        # initialize the game and game creation resources
        pygame.init()

        # window, import settings from settings.py script
        self.settings = Settings()

        # set game to full screen
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # change settings dimensions to match screen size
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height 

        # set title of window
        pygame.display.set_caption("Alien Invasion")

        # init ship
        self.ship = Ship(self)
    
    # function to invoke the main game loop for in game updates
    def runGame(self):

        # start main game loop
        while True:

            # check for input events while loop
            self._check_events()

            # ship update function running in game loop
            self.ship.update()

            # debug the ship position for testing
            # print(self.ship.x)
            
            # update screen while looping
            self._update_screen()
    
    # function to check for keypresses and mouse events
    def _check_events(self):

            # watch for keyboard and mouse events 
            for event in pygame.event.get():
                
                # for closing window 
                if event.type == pygame.QUIT:
                    sys.exit()

                # when key on keyboard is pressed down
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

                # when key on key board is released
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    # function to respond to key presses
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # set ship movement flag for right movement true
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # same but for left movement
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            # close game on pressing 'q'
            sys.exit()

    # function to respond to key releases
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

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
