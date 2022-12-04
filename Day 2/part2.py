import enum

class Hand(enum.Enum):
    Rock = 1
    Paper = 2
    Scissor = 3

    def GetHand(letter):
        if letter == "A" or letter == "X":
            return Hand.Rock
        elif letter == "B" or letter == "Y":
            return Hand.Paper
        elif letter == "C" or letter == "Z":
            return Hand.Scissor
        else:
            raise ValueError("Invalid letter")

    def CalculateMatchScore(oppenents_hand, outcome):
        score = 0
        
        if outcome == "Z": # win
            score += 6
            if opponents_hand == Hand.Rock:
                score += Hand.Paper.value
            elif opponents_hand == Hand.Paper:
                score += Hand.Scissor.value
            elif opponents_hand == Hand.Scissor:
                score += Hand.Rock.value
            else:
                raise ValueError("Invalid letter")
        elif outcome == "Y": # draw
            score += 3 + opponents_hand.value
        elif outcome == "X": # lose
            if opponents_hand == Hand.Rock:
                score += Hand.Scissor.value
            elif opponents_hand == Hand.Paper:
                score += Hand.Rock.value
            elif opponents_hand == Hand.Scissor:
                score += Hand.Paper.value
            else:
                raise ValueError("Invalid letter")
        else:
                raise ValueError("Invalid letter")
        
        return score

with open("Day 2\input.txt") as input:
    total_score = 0

    for line in input:
        opponents_hand = Hand.GetHand(line[0])
        outcome = line[2]

        total_score += Hand.CalculateMatchScore(opponents_hand, outcome)
    
    print(total_score)
