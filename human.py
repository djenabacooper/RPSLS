from players import Player
class Human(Player):
    def __init__(self, player_name) -> None:
        super().__init__(player_name)
        self.difficulty_level = 5
        

    def choose_gesture(self):
        user_chose = False
        print(f'Here are the gesture options: {self.gestures}. Type 1 for Rock, 2 for Paper, 3 for Scissors, 4 for Lizard, 5 for Spock')
        while user_chose == False:
            user_input = int(input())
            if user_input == 0:
                user_chose = True
                print("Player chooses Rock")
                self.player_gesture = "Rock"
            elif user_input == 1:
                print("Player chooses Paper")
                user_chose = True
                self.player_gesture = "Paper"
            elif user_input == 2:
                print("Player chooses Scissors")
                user_chose = True
                self.player_gesture = "Scissors"
            elif user_input == 3:
                print("Player chooses Lizard")
                user_chose = True
                self.player_gesture = "Lizard"
            elif user_input == 4:
                self.player_gesture = "Spock"
                print("Player chooses Spock")
                self.player_gesture = "Spock"
                user_chose = True
            else:
                print('Please input a number between 0-')
