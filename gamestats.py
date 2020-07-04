# track stats for enemies and ship interaction
class GameStats:

    # init the stats
    def __init__(self, ai_game):
        
        self.settings = ai_game.settings
        self.reset_stats()

        # start the invasion in an inactive state
        self.game_active = False

        # high score should remain untouched
        self.high_score = 0

    # function to reset stats at any point in game
    def reset_stats(self):

        # initialize stats 
        self.ships_left = self.settings.ship_limit

        # reset player score to 0
        self.score = 0

        # reset levle to 1
        self.level = 1