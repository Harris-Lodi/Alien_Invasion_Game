# import built in modules
import sys
from time import sleep
import pygame
# import other classes
from settings import Settings
from ship import Ship
from bullet import Bullet
from enemy import Enemy
from gamestats import GameStats

# Overall class to manage game assets and behavior, cont on page 280
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

        # create an instance of game statistics
        self.stats = GameStats(self)

        # init ship
        self.ship = Ship(self)

        # init and group bullets
        self.bullets = pygame.sprite.Group()

        # init and group enemies
        self.enemies = pygame.sprite.Group()

        # init enemy fleet
        self._create_fleet()
    
    # function to invoke the main game loop for in game updates
    def runGame(self):

        # start main game loop
        while True:

            # check for input events while loop
            self._check_events()

            # run the following only is the game stat is active
            if self.stats.game_active:

                # ship update function running in game loop
                self.ship.update()

                # run bullet updates
                self._update_bullets()

                # run enemy updates
                self._update_enemies()

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
        elif event.key == pygame.K_SPACE:
            # fire bullets
            self._fire_bullet()

    # function to respond to key releases
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # check if any enemies reach the bottom of screen
    def _check_enemies_bottom(self):

        screen_rect = self.screen.get_rect()
        for enemy in self.enemies.sprites():
            if enemy.rect.bottom >= screen_rect.bottom:
                # treat this event same as if the ship got hit
                self._ship_hit()
                break

    # function to run code related to ship health and behavior
    def _ship_hit(self):

        # interact when the ship lives are above 0
        if self.stats.ships_left > 0:

            # respond to the ship being hit by enemies
            # decrement ship help
            self.stats.ships_left -= 1

            # get rid of any remaining enemies and bullets
            self.enemies.empty()
            self.bullets.empty()

            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # pause game for a while
            sleep(0.5)

        else:
            self.stats.game_active = False

    # a function to update bullets and the entire code in one go
    def _update_bullets(self):

        # add bullets to game loop
        self.bullets.update()

        # get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

        # have bullet collison code run on bullet update
        self._check_bullet_enemy_collisions()

    # a function to respond to bullet collisons
    def _check_bullet_enemy_collisions(self):

        # respond to bullet-enemy collisions
        # check for any bullets that have hit enemies
        # if so, get rid of the bullet and the enemy
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)

        # destroy exisitng bullets and repopulate enemies if entire fleet is dead
        if not self.enemies:

            self.bullets.empty()
            self._create_fleet()

    # a function to update enemies
    def _update_enemies(self):

        # check if the fleet is at an edge
        # then update the positions of all enemies in the fleet
        self._check_fleet_edges()

        # update position of all enemies in fleet
        self.enemies.update()

        # look for enemy-ship collisions, for player to loose health and the game
        if pygame.sprite.spritecollideany(self.ship, self.enemies):
            self._ship_hit()

        # if any enemy hits the screen bottom
        self._check_enemies_bottom()

    # create a fleet of enemies
    def _create_fleet(self):

        # make enemy to do the following calculations
        enemy = Enemy(self)
        # find number of enemies per row, spacing btw enemies is one enemy unit
        # find the enemy height to for y axis columns
        enemy_width, enemy_height = enemy.rect.size
        # available_space_x is the space on either side of the row until the screen borders
        available_space_x = self.settings.screen_width - (2 * enemy_width)
        # space btw enemies = available_space floor divided by twice the width of an enemy
        number_enemies_x = available_space_x // (2 * enemy_width)

        # determine the # of rows of enemies to fit on screen
        ship_height = self.ship.rect.height
        # calculate the available vertical space above ship
        available_space_y = (self.settings.screen_height -
            (3 * enemy_height) - ship_height)
        # calc the number of rows from available_height
        number_rows = available_space_y // (2 * enemy_height)

        # create the full fleet of enemies
        for row_number in range(number_rows):
            for enemy_number in range(number_enemies_x):
                self._create_enemy(enemy_number, row_number)

    # function to create enemy and place it in row
    def _create_enemy(self, enemy_number, row_number):

        # create an enemy from the class to add it in fleet
        enemy = Enemy(self)
        # re-create enemy_size just like from _create_fleet
        enemy_width, enemy_height = enemy.rect.size
        # calculate the space after current enemy to place the next one
        enemy.x = enemy_width + 2 * enemy_width * enemy_number
        # set the above calc as their position for this unit in for loop
        enemy.rect.x = enemy.x 
        # position enemies vertically based on following calculations
        enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * row_number
        # create an enemy and place it in row
        self.enemies.add(enemy)

    # function to run code when an enemy from fleet reaches an edge
    def _check_fleet_edges(self):

        # if an enemy sprite touches screen edge, have it change direction
        for enemy in self.enemies.sprites():
            if enemy.check_edges():
                self._change_fleet_direction()
                break
    
    # function to run code upon fleet's direction change
    def _change_fleet_direction(self):

        # drop entire fleet and change fleet direction
        for enemy in self.enemies.sprites():
            enemy.rect.y += self.settings.fleet_drop_speed
        
        # change direction to either -1 or 1 at each invoke
        self.settings.fleet_direction *= -1

    # function to fire bullets
    def _fire_bullet(self):

        # create bullet and add it to bullets group, only allow limited # of bullets
        if len(self.bullets) < self.settings.bullets_allowed:

            new_Bullet = Bullet(self)
            self.bullets.add(new_Bullet)

    # function to update screen in loop
    def _update_screen(self):

            # redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            # position ship
            self.ship.blitme()

            # draw bullets from bullet group
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            
            # draw enemies
            self.enemies.draw(self.screen)
            
            # make the most recent drawn screen visible
            pygame.display.flip()

# run class and game
if __name__ == '__main__':

    # make a game instance and run the game
    ai = alienInvasion()
    ai.runGame()
