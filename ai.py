from players import Player
from random import random
class AI(Player):
    def __init__(self) -> None:
        super().__init__('skinjob',random.choice(self.player_gesture))
        
    
    def choose_gesture(self):
        self.player_gesture = random.choice(self.player_gesture)

def name_gest(self):
    print(self.player_name, self.player_gesture)
