from players import Player
import random
from gestures import Gesture
class AI(Player):
    def __init__(self) -> None:
        super().__init__('skinjob')
        
    
    def choose_gesture(self):
        self.player_gesture = random.choice(self.gestures)
        print(f'Player chooses {self.player_gesture}')


def name_gest(self):
    print(self.player_name, self.player_gesture)
