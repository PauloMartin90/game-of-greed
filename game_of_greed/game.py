from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from random import randint

class Game:
    def default_roller():
        return (randint(1,6),randint(1,6))

    def play_dice(roller=default_roller):

        while True:
            print("(r)oll again, (b)ank your points or (q)uit:")
            choice = input("> ")
            if choice == "q":
                print("OK, bye")
                break
            else:
                roll = roller()
                roll_str = ""
                for num in roll:
                    roll_str += str(num) + " "
                roll_str_var = f"*** {roll_str} ***"
                print(roll_str_var)
                return roll_str_var
                

    def start_game(self):
        print("Starting round 1")
        print("Rolling 6 dice...")
        round_roll = GameLogic.roll_dice(6)
        print("*** 3 2 5 4 3 3 ***")
        print("Enter dice to keep, or (q)uit:")

    def play(self, roller = None):
        self._roller = roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        ans = input("> ")
        
        if ans == "n":
            print("OK. Maybe another time")
            
        if ans == "y" :
            self.start_game()
            
        ans2 = input("> ")
        if ans2 == "5":
            score = GameLogic.calculate_score(ans2)
            print(f"You have {score} unbanked points and 5 dice remaining")
            
        if ans2 == "q":
            print("Thanks for playing. You earned 0 points")
            return

        print("(r)oll again, (b)ank your points or (q)uit:")

        ans3 = input("> ")
        if ans3 == "b":
            print(f"You banked 50 points in round 1")
            print("Total score is 50 points")

        print("Starting round 2")
        print("Rolling 6 dice...")
        print("*** 6 4 5 2 3 1 ***")
        print("Enter dice to keep, or (q)uit:")

        ans4 = input("> ")
        if ans4 == "q":
            print("Thanks for playing. You earned 50 points")