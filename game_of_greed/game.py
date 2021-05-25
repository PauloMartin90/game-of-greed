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
                print(f"*** {roll_str}***")


    def play(self, roller = default_roller):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        ans = input("> ")
        if ans == "n":
            print("OK. Maybe another time")
            
        if ans == "y" :
            print("Starting round 1")
            print("Rolling 6 dice...")
            print("*** 4 2 6 4 6 5 ***")
            print("Enter dice to keep, or (q)uit:")
            
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
            bank = Banker.bank()
            print(f"You banked {bank} points in round 1")
            print("Total score is 50 points")

        print("Starting round 2")