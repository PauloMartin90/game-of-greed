class GameLogic:
    def __init__(self):
        pass

    def calculate_score(roll):
        score = 0
        if roll.count(5) == 3:
            score += 500
            for i in roll:
                if i == 1:
                    score += 100
            return score
        if roll.count(1) == 3:
            score += 1000
            for i in roll:
                if i == 5:
                    score += i * 10
            return score
        for i in roll:
            if i == 5:
                score += i * 10
            if i == 1:
                score += i * 100

        return score


# merging tuples together
# def merge(template, parts):
# merged = template.format(*parts)
# return merged
