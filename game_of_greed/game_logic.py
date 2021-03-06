from collections import Counter
import random


class GameLogic:
    import random


scoresheet = {
    "1": {"1": 100, "2": 200, "3": 1000, "4": 2000, "5": 3000, "6": 4000},
    "2": {"1": 0, "2": 0, "3": 200, "4": 400, "5": 600, "6": 800},
    "3": {"1": 0, "2": 0, "3": 300, "4": 600, "5": 900, "6": 1200},
    "4": {"1": 0, "2": 0, "3": 400, "4": 800, "5": 1200, "6": 1600},
    "5": {"1": 50, "2": 100, "3": 500, "4": 1000, "5": 1500, "6": 2000},
    "6": {"1": 0, "2": 0, "3": 600, "4": 1200, "5": 1800, "6": 2400},
    "special": {"straight": 1500, "three pair": 1500},
}


class GameLogic:
    @staticmethod
    def roll_dice(dice):
        total = []
        while dice > 0:
            roll = random.randint(1, 6)
            total.append(roll)
            dice -= 1
        return total

    @staticmethod
    def calculate_score(dice):
        counter = 0
        occurrences = {}
        for num in dice:
            times_rolled = dice.count(num)
            occurrences[num] = times_rolled

        if sorted(dice) == [1, 2, 3, 4, 5, 6]:
            counter += scoresheet["special"]["straight"]
            return counter

        keys = list(occurrences.keys())

        if len(keys) == 3:
            if (
                (occurrences[keys[0]] == 2)
                and (occurrences[keys[1]] == 2)
                and (occurrences[keys[2]] == 2)
            ):
                counter += scoresheet["special"]["three pair"]
                return counter

        for num in occurrences:
            counter += scoresheet[str(num)][str(occurrences[num])]

        return counter

    @staticmethod
    def validate_keepers(roll, keepers):
        return not Counter(keepers) - Counter(roll)
