import pygame.font
from pygame.sprite import Group

from ship import Ship

# class to display player's score on screen and manage the data
class Scoreboard:

    # init scorekeeping attributes for reporting score
    def __init__(self, ai_game):

        self.ai_game = ai_game

        self.screen = ai_game.screen 
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring info
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prep the initial score images, and player lives
        self.prep_lives()
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    # function to turn the score to a rendered image
    def prep_score(self):
        
        # round our score to the nearest 10, and the format line will insert commas every 3 places
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # display the score at the top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    # a function to track and render the highest score
    def prep_high_score(self):

        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    # a function to check and compare high scores
    def check_high_score(self):

        # check if there is a new high score
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    # function to display current level
    def prep_level(self):

        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    # function to display the lives left
    def prep_lives(self):

        self.lives = Group()
        for life_number in range(self.stats.ships_left):
            life = Ship(self.ai_game)
            life.rect.x = 10 + life_number * life.rect.width
            life.rect.y = 10
            self.lives.add(life)

    # a function to draw the score value to screen, also remaining lives as well
    def show_score(self):

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.lives.draw(self.screen)