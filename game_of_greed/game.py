from typing import Counter
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
        self.cheater = False

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
            if not self.cheater:
                print(f"Rolling {num_dice} dice...")
                self.cheater = False
            roll = self.roller(num_dice)
            roll_string = " ".join([str(i) for i in roll])
            print(f"*** {roll_string} ***")
            
            self.handle_keepers(roll_string, round_score, num_dice)
            # print("(r)oll again, (b)ank your points or (q)uit:")
                
            ans3 = input("> ")
            if ans3 == "r":
                if num_dice == 0:
                    num_dice = 6
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
            
    def handle_keepers(self, roll_string, round_score, num_dice):
        print("Enter dice to keep, or (q)uit:")
            # Changes for p
        ans2 = input("> ")

        if ans2 == "q":
            self.quit_game()

        while True:
            # gather keepers
            while not GameLogic.validate_keepers(roll_string, ans2):
                # we need to make a keep rolling method
                self.keep_rolling(ans2, round_score, num_dice)
                print("(r)oll again, (b)ank your points or (q)uit:")
            else:
                self.cheater = True
                print("Cheater!!! Or possibly made a typo...")


    def keep_rolling(self, ans2, round_score, num_dice):
        dice_values = tuple(int(num) for num in ans2)
        round_score += GameLogic.calculate_score(dice_values)
        self.banker.shelf(round_score)
        num_dice -= len(ans2)
        print(
            f"You have {self.banker.shelved} unbanked points and {num_dice} dice remaining"
        )

    def score_round(self, string):
        dice = []
        for num in string:
            dice.append(num)

        result = []
        result.append(6 - len(dice))
        dice = tuple(dice)
        result.append(GameLogic.calculate_score(dice))

        return result

# acp