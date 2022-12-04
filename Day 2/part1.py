# Question: What would your total score be if everything goes exactly according to your strategy guide?
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

    def CalculateMatchScore(my_hand, opponents_hand):
        score = 0

        if my_hand == Hand.Rock and opponents_hand == Hand.Scissor or my_hand == Hand.Paper and opponents_hand == Hand.Rock or my_hand == Hand.Scissor and opponents_hand == Hand.Paper: # win
                score += 6 
        elif opponents_hand == my_hand: # draw
            score += 3 

        score += my_hand.value

        return score

with open("Day 2\input.txt") as input:
    total_score = 0

    for line in input:
        opponents_hand = Hand.GetHand(line[0])
        my_hand = Hand.GetHand(line[2])

        total_score += Hand.CalculateMatchScore(my_hand, opponents_hand)
    
    print(total_score)
