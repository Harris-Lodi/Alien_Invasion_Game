import pygame
from pygame.sprite import Sprite

# a class to manage the ship
class Ship(Sprite):

    # init the ship and set starting position, and settings
    def __init__(self, ai_game):

        # init the super class
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get it's box
        self.image = pygame.image.load('Images/spaceship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom of the screen
        self.initpos = self.screen_rect.midbottom
        self.rect.midbottom = self.initpos

        # store a decimal value for the ship's horizontal positions
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False
    
    # update the ship's position based on movement flag
    def update(self):

        # update the ship's x value, and limit it between screen boundaries
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        
        # update rect object from self.x
        self.x = self.rect.x
    
    # draw the ship at it's curent location
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # function to position ship upon respawn
    def center_ship(self):

        # center ship on screen
        self.rect.midbottom = self.initpos
        self.x = float(self.rect.x)
    
    