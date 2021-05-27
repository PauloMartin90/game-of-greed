from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from random import randint
import sys


class Game:
    def __init__(self, num_rounds=20):
        self.banker = Banker()
        self.num_rounds = num_rounds
        self.round_num = 0
        self.roller = None
        self.done = False

    def play(self, roller=None):
        self.roller = roller or GameLogic.roll_dice
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        start_game = input("> ")
        if start_game == "n":
            print("OK. Maybe another time")

        elif start_game == "y":
            self.round_num = 0
            while not self.done:
                self.round_num += 1
                self.start_game()

        else:
            pass
            # ask client what to do in this case

    def start_game(self):
        while self.round_num <= self.num_rounds and self.done == False:
            self.play_round(self.round_num)
            self.round_num += 1  # this is the second place for this
            if self.done == False:
                print(f"Total score is {self.banker.balance} points")
        self.quit_game()

    def quit_game(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit()

    def play_round(self, round_num, num_dice=6):
        keep_rolling = True
        print(f"Starting round {self.round_num}")
        round_score = 0
        # loop here?
        while keep_rolling:
            print(f"Rolling {num_dice} dice...")
            roll = self.roller(num_dice)
            roll_string = " ".join([str(i) for i in roll])
            print(f"*** {roll_string} ***")
            print("Enter dice to keep, or (q)uit:")

            ans2 = input("> ")
            if ans2.isnumeric():
                # we need to make a keep rolling method
                dice_values = tuple(int(num) for num in ans2)

                round_score += GameLogic.calculate_score(dice_values)

                self.banker.shelf(round_score)
                num_dice -= len(ans2)
                print(
                    f"You have {self.banker.shelved} unbanked points and {num_dice} dice remaining"
                )

            elif ans2 == "q":
                self.quit_game()

            print("(r)oll again, (b)ank your points or (q)uit:")

            ans3 = input("> ")
            if ans3 == "r":

                pass
                # print(f"Rolling {num_dice} dice...")
                # self.banker.shelf(score)
                # self.play_round(self.round_num, num_dice)
            if ans3 == "b":
                round_points = self.banker.bank()
                print(f"You banked {round_points} points in round {self.round_num}")
                keep_rolling = False

            if ans3 == "q":
                self.quit_game()

    def keep_rolling():
        pass

    def score_round(self, string):
        dice = []
        for num in string:
            dice.append(num)

        result = []
        result.append(6 - len(dice))
        dice = tuple(dice)
        result.append(GameLogic.calculate_score(dice))

        return result
