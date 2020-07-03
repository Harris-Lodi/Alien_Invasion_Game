import pygame
from pygame.sprite import Sprite

# a class to represent a single enemy in the fleet
class Enemy(Sprite):

    # init the enemy and it's starting position
    def __init__(self, ai_game):

        # just like with bullet, initialize the Sprite super class
        # and set enemy to main game screen
        # import settings for enemy from ai_game
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the enemy image and set it's rect attribute
        self.image = pygame.image.load('Images/enemy.bmp')
        self.rect = self.image.get_rect()

        # start each new enemy near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the enemies exact horizontal position
        self.x = float(self.rect.x)

    # function to check if enemy is at edge of screen
    def check_edges(self):

        # return true if enemy is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >=  screen_rect.right or self.rect.left <= 0:
            return True

    # enemy update function
    def update(self):

        # move enemy to the right or left depending on fleet_direction
        self.x += (self.settings.enemy_speed * self.settings.fleet_direction)
        # update position and record it to this instance class
        self.rect.x = self.x


