from collections import Counter
import random


class GameLogic:
    def __init__(self):
        pass

    def calculate_score(roll):
        score = 0
        if (
            roll.count(1)
            == 1 & roll.count(2)
            == 1 & roll.count(3)
            == 1 & roll.count(4)
            == 1 & roll.count(5)
            == 1 & roll.count(6)
            == 1
        ):
            score += 1500
            return score
        if roll.count(1) == 3:
            score += 1000
            for i in roll:
                if i == 5:
                    score += i * 10
            return score
        for i in roll:
            if roll.count(i) == 6:
                if i == 1:
                    score += 4000
                    return score
                else:
                    score += i * 100 * 4
                    return score
            if roll.count(i) == 5:
                if i == 1:
                    score += 3000
                    if roll.count(5) == 1:
                        score += 50
                    return score
                else:
                    score += i * 100 * 3
                    if roll.count(5) == 1:
                        score += 50
                    if roll.count(1) == 1:
                        score += 100
                    return score
            if roll.count(i) == 4:
                if i == 1:
                    score += 2000
                    return score
                else:
                    score += i * 100 * 2
                    return score
            if roll.count(i) == 3:
                if i == 1:
                    score += 1000
                    return score
                else:
                    score += i * 100
                    return score
            # if roll.count(i) == 2 & len(roll.count() == 3):
            #     score += 1500
            #     return score
            if i == 5:
                score += i * 10
            if i == 1:
                score += i * 100
        return score

    def roll_dice(number_of_rolls):
        values = []
        if number_of_rolls >= 1:
            values.append(random.randint(1, 6))
            if number_of_rolls >= 2:
                values.append(random.randint(1, 6))
                if number_of_rolls >= 3:
                    values.append(random.randint(1, 6))
                    if number_of_rolls >= 4:
                        values.append(random.randint(1, 6))
                        if number_of_rolls >= 5:
                            values.append(random.randint(1, 6))
                            if number_of_rolls == 6:
                                values.append(random.randint(1, 6))
        return values
