#from typing_extensions import Self
from players import Player
from human import Human
from ai import AI
from gestures import Gesture
from random import random

class Game:
    def __init__(self,):
        self.player1 = Human('William')
        self.player2 = AI()
        # self.player_gesture = Gesture()
        # self.round_winner = round_winner
        pass

    def run_game(self):
        #self.Rules()
        # self.choose_players()
        self.Round_opps()
        

    def Rules(self):
      print('''Welcome to the Game!!! \n
        Here are the rules: \n
        Rock crushes Scissors \n
        Paper covers Rock \n
        Rock crushes Lizard \n
        Lizard poisons Spock \n
        Spock smashes Sciossors \n
        Scissors decapitates Lizard \n
        Paper disproves Spock \n
        Spock vaporizes Rock''')

    
    def Round_opps(self):
        player_type = input('Type 1 for Human vs Human, type 2 for AI vs AI, type 3 for Human vs AI')
        if player_type == "1":
            self.player1 = Human("Bob")
            self.player2 = Human('John')  
        elif player_type == '2':
            self.player1 = AI()
            self.player2 = AI() #player_two
        else:
            self.player1 = AI()
            self.player2 = Human("Player 2")

        #self.player1.choose_gesture()
        #self.player2.choose_gesture()

        winner = ''
        while winner =='':
            self.player1.choose_gesture()
            self.player2.choose_gesture()
            if self.player1.score == 3:
                winner = self.player1
            elif self.player2.score == 3:
                winner = self.player2
            if self.player1.player_gesture == "Rock" and self.player2.player_gesture == "Scissors":
                self.player1.score += 1
            elif self.player2.player_gesture == "Rock" and self.player1.player_gesture == "Scissors":
                self.player2.score +=1 
            if self.player1.player_gesture == "Paper" and self.player2.player_gesture == "Rock":
                self.player1.score += 1
            elif self.player2.player_gesture == "Paper" and self.player1.player_gesture == "Rock":
                self.player2 +=1
            if self.player1.player_gesture == "Rock" and self.player2.player_gesture == "Lizard":
                self.player1.score += 1
            elif self.player2.player_gesture == "Rock" and self.player1.player_gesture == "Lizard":
                self.player2 +=1
            if self.player1.player_gesture == "Lizard" and self.player2.player_gesture == "Spock":
                self.player1.score += 1
            elif self.player2.player_gesture == 'Lizard' and self.player1.player_gesture == "Spock":
                self.player2.score +=1
            if self.player1.player_gesture == "Spock" and self.player2.player_gesture == "Scissors":
                self.player1.score += 1
            elif self.player2.player_gesture == "Spock" and self.player1.player_gesture == "Scissors":
                self.player2.score +=1
            if self.player1.player_gesture == "Scissors" and self.player2.player_gesture == "Lizard":
                self.player1.score += 1
            elif self.player2.player_gesture == "Scissors" and self.player1.player_gesture == "Lizard":
                self.player2.score +=1
            if self.player1.player_gesture == "Paper" and self.player2.player_gesture == "Spock":
                self.player1.score += 1
            elif self.player2.player_gesture == "Paper" and self.player1.player_gesture == "Spock":
                self.player2.score +=1
            if self.player1.player_gesture == "Spock" and self.player2.player_gesture == "Rock":
                self.player1.score += 1
            elif self.player2.player_gesture == "Spock" and self.player1.player_gesture == "Rock":
                self.player2.score +=1
            if self.player1.score == 3:
                winner = self.player1.player_name
            elif self.player2.score == 3:
                winner = self.player2.player_name
        print(f'Winner is {winner}!')
 
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

    


#my_game = Game()
#my_game.run_game()