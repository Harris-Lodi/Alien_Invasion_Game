import pygame

# a class to manage the ship
class Ship:

    # init the ship and set starting position
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get it's box
        self.image = pygame.image.load('Images/spaceship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    # draw the ship at it's curent location
    def blitme(self):
        self.screen.blit(self.image, self.rect)