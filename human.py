from players import Player
class Human(Player):
    def __init__(self, player_name) -> None:
        super().__init__(player_name)
        self.difficulty_level = 5
        

    def choose_gesture(self):
        user_chose = False 
        while user_chose == False:
            user_input = int(input())
            if user_input == 0:
                user_chose = True
                print("Player chooses Rock")
                self.player_gesture = "Rock"
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
                    self.player_gesture = "Spock"
                    print("Player chooses Spock")
                    user_chose = True
            else:
                print('Please input a number between 0-')
