from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from random import randint


class Game:
    def __init__(self, num_rounds=20):
        self.banker = Banker()
        self.num_rounds = num_rounds
        self.round_num = 0
        self.roller = None
        self.done = False

    def default_roller():
        return (randint(1, 6), randint(1, 6))

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

    def play(self, roller=None):
        self.roller = roller or GameLogic.roll_dice
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        start_game = input("> ")
        if start_game == "n":
            print("OK. Maybe another time")

        elif start_game == "y":

            round = 1
            while not self.done:
                self.play_round(round)
                round += 1

        else:
            pass
            # ask client what to do in this case

    def play_round(self, round):
        num_dice = 6

        print(f"Starting round {round}")
        print(f"Rolling {num_dice} dice...")
        roll = self.roller(6)
        roll_string = " ".join([str(i) for i in roll])
        print(f"*** {roll_string} ***")
        print("Enter dice to keep, or (q)uit:")

        ans2 = input("> ")
        if ans2.isnumeric():
            # dice_values = []
            # for num in ans2:
            #     dice_values.append(int(num))

            # dice_values_tuple = tuple(dice_values)
            # 3335 -> GameLogic.calculate_score

            dice_values = tuple(int(num) for num in ans2)

            score = GameLogic.calculate_score(dice_values)

            self.banker.shelf(score)
            num_dice -= len(ans2)
            print(
                f"You have {self.banker.shelved} unbanked points and {num_dice} dice remaining"
            )

        elif ans2 == "q":
            print(f"Thanks for playing. You earned {self.banker.balance} points")
            self.done = True
            return

        print("(r)oll again, (b)ank your points or (q)uit:")

        ans3 = input("> ")
        if ans3 == "b":
            round_points = self.banker.bank()
        if ans3 == "q":
            self.done = True
        print(f"You banked {round_points} points in round {round}")
        print(f"Total score is {self.banker.balance} points")

    def score_round(self, string):
        dice = []
        for num in string:
            dice.append(num)

        result = []
        result.append(6 - len(dice))
        dice = tuple(dice)
        result.append(GameLogic.calculate_score(dice))

        return result
