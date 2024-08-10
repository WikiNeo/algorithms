from typing import List
from collections import Counter


def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    # check the if the hand is divisible first
    if len(hand) % groupSize != 0:
        return False

    # let's count the cards first
    card_count = Counter(hand)
    # and sort the result
    sorted_card = sorted(card_count)

    # let's start with the min one
    for card in sorted_card:
        # if we still have cards
        if card_count[card] > 0:
            count = card_count[card]
            # check if we can get the consecutive array
            for i in range(card, card + groupSize):
                if card_count[i] < count:
                    return False
                card_count[i] -= count

    return True
