
class GameLogic:
    def __init__(self):
        pass

    def calculate_score(roll):
        score = 0

        try:
            if roll.count(5) == 1:
                score += 50

            if roll.count(1) == 1 or roll.count(5) == 2:
                score += 100

            return score

        except:
            print("something")


    def roll_dice(roll):
        values = []

        for i in roll:
            values.append(1)
        
        return values





            



