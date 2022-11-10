#from typing_extensions import Self
from players import Player
from gestures import Gesture
from random import random

class Game:
    def __init__(self,):
        self.player1 = Player('player_one')
        self.player2 = Player('player_two')
        # self.player_gesture = Gesture()
        # self.round_winner = round_winner
        pass

    def run_game(self):
        #self.Rules()
        # self.choose_players()
        self.Round_opps()

    def Rules(self):
      user_chose = False 
      while user_chose == False:
       user_input = int(input())
       if user_input == 0:
           user_chose = True
           print("Player chooses Rock")
       elif user_input == 1:
           print("Player chooses Paper")
           user_chose = True
       elif user_input == 2:
           print("Player chooses Scissors")
           user_chose = True
       elif user_input == 3:
           print("Player chooses Lizard")
           user_chose = True
       elif user_input == 4:
            print("Player chooses Spock")
            user_chose = True
       else:
           print('Please input a number between 0-')

    
    def Round_opps(self):

        self.player1.choose_gesture()
        self.player2.choose_gesture()


        if self.player1.player_gesture == "Spock" and self.player2.player_gesture == "Rock":
            self.player1.score += 1
            print("Yee")

        # active_round = True
        # round_count = 0
        # if round_count < 3:
        #     round_count =+ 1
        #     self.Rules()
        #     self.Rules()
        # else:
        #     print("we're done")        
    




   # def Rules_with_tryCatch(self):
   #    user_chose = False 
   #    while user_chose == False:
   #        try:
   #            user_input = int(input())
   #            print(f'Player chooses ${self.player_gesture.gest_opps[user_input]}')
   #            user_chose = True
   #        except:
   #            print("Error does not compute")
   # 
   # Rules_with_tryCatch(Gesture)

    


my_game = Game()
my_game.run_game()