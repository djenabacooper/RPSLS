from players import Player
import random
from gestures import Gesture
class AI(Player):
    def __init__(self) -> None:
        super().__init__('skinjob')
        
    
    def choose_gesture(self):
        print(f'Here are the gesture options: {self.gestures}. Type 1 for Rock, 2 for Paper, 3 for Scissors, 4 for Lizard, 5 for Spock')
        self.player_gesture = random.choice(self.gestures)
        print(f'Player chooses {self.player_gesture}')


def name_gest(self):
    print(self.player_name, self.player_gesture)
