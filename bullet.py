import pygame
from pygame.sprite import Sprite

# A class to manage the bullets fired from the ship, extends Sprite class from pygame
class Bullet(Sprite):

    # create a bullet object at the ship's current position
    def __init__(self, ai_game):
        
        # super().__init__() runs __init__ for Sprite class
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullet rect at (0, 0) and set to ship position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store bullet position as decimal value
        self.y = float(self.rect.y)

    # Move the bullet up the screen
    def update(self):

        # update the decimal position of the bullet
        self.y -= self.settings.bullet_speed

        # update the rect position
        self.rect.y = self.y

    # Draw the bullet to screen
    def draw_bullet(self):

        pygame.draw.rect(self.screen, self.color, self.rect)

        
