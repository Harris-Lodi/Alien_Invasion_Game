class Settings:
    # A class to store all settings for the game

    def __init__(self):

        # initialize game settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # bullet settings, for their design
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # enemy settings
        self.enemy_speed = 1.0
        self.fleet_drop_speed = 30
        # fleet direction of 1 represents right, -1 is left
        self.fleet_direction = 1
        # scoring by enemy kills
        self.enemy_points = 50

        # player level up settings
        self.speedup_scale = 1.2

        # enemy score count rises with level rise
        self.score_scale = 1.5

        # init settings to change through out the game
        self.initialize_dynamic_settings()

    # a function to reset speed settings as game goes on
    def initialize_dynamic_settings(self):

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.enemy_speed = 1.0

        # fleet direction is right when 1, left when -1
        self.fleet_direction = 1

    # function to increase speed settings and enemy point values
    def increase_speed(self):

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.enemy_speed *= self.speedup_scale

        self.enemy_points = int(self.enemy_points * self.score_scale)
        print(self.enemy_points) # debug scoring
