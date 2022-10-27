from rounds import Round

class Game(Round):
    def __init__(self, player, player_gesture, round_winner, game_winner):
        super().__init__(player, player_gesture, round_winner)
        self.player = player
        self.player_gesture = player_gesture
        self.game_winner = game_winner
    