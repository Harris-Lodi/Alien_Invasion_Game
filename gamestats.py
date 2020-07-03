# track stats for enemies and ship interaction
class GameStats:

    # init the stats
    def __init__(self, ai_game):

        # star the invasion in an active state
        self.game_active = True
        
        self.settings = ai_game.settings
        self.reset_stats()

    # function to reset stats at any point in game
    def reset_stats(self):

        # initialize stats 
        self.ships_left = self.settings.ship_limit