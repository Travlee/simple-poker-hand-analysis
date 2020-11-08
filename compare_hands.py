#!/usr/bin/python3

"""
    author: Travis Lee Presnell
    name: Poker-hand-winner-decider-app!
    date: 04 November, 2020
    notes: Swept Full Stack Developer Position - Test 1

"""

import sys


CARD_SCORES = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "*": 0
}


HAND_SCORES = {
    "four-of-a-kind": 7,
    "full house": 6,
    "straight": 5,
    "three-of-a-kind": 4,
    "two pair": 3,
    "pair": 2,
    "high card": 1
}


def main(hand_one, hand_two):

    result = compare_hands(hand_one, hand_two)
    print(result)


def compare_hands(hand_one, hand_two):
    if not valid_hand(hand_one) or not valid_hand(hand_two):
        print(
            "Invalid hands: {hand_one}, {hand_two}".format(
                hand_one=hand_one,
                hand_two=hand_two))
        exit()

    hand_one_analysis = analyze_hand(hand_one)
    hand_two_analysis = analyze_hand(hand_two)

    winner_char = get_winner(
        hand_one_analysis,
        hand_two_analysis
    )

    return(
        "{hand_one} vs {hand_two}: {hand_one} {hand_one_class} {winner_char} {hand_two} {hand_two_class}".format(
            hand_one=hand_one, hand_two=hand_two, hand_one_class=hand_one_analysis[
                "hand_class"], hand_two_class=hand_two_analysis["hand_class"], winner_char=winner_char
        ))


def get_winner(hand_one_analysis, hand_two_analysis):
    """Returns a comparison symbol for two hands"""

    hand_one_score = hand_one_analysis["hand_score"]
    card_one_score = hand_one_analysis["card_score"]
    hand_one_highest = hand_one_analysis["hand_highest"]
    hand_one_wildcard = hand_one_analysis["wildcard"]
    hand_two_score = hand_two_analysis["hand_score"]
    card_two_score = hand_two_analysis["card_score"]
    hand_two_highest = hand_two_analysis["hand_highest"]
    hand_two_wildcard = hand_two_analysis["wildcard"]

    if hand_one_score > hand_two_score:
        return ">"
    elif hand_one_score < hand_two_score:
        return "<"
    else:
        if hand_one_highest > hand_two_highest:
            return ">"
        elif hand_one_highest < hand_two_highest:
            return "<"
        else:
            if card_one_score > card_two_score and not hand_two_wildcard:
                return ">"
            elif card_one_score < card_two_score and not hand_one_wildcard:
                return "<"
            else:
                return "=="


def analyze_hand(hand):
    """Analyzes given hand_count"""

    hand_count = count_cards(hand)
    fours = 0
    threes = 0
    pairs = 0
    sequence = []

    result = {
        "hand_class": "",
        "hand_score": 0,
        "card_score": 0,
        "hand_highest": 0,
        "wildcard": False
    }

    if "*" in hand_count:
        result["wildcard"] = True

    for card in hand_count:
        count = hand_count[card]
        result["card_score"] += CARD_SCORES[card]

        # ? Fours
        if count == 4:
            result = set_hand_analysis(
                result, hand_name="four-of-a-kind")
            result["card_score"] = CARD_SCORES[card]
            result["hand_highest"] = find_card_score(
                result["hand_highest"],
                CARD_SCORES[card]
            )
            fours = 1

        elif count == 3:
            result = set_hand_analysis(
                result, hand_name="three-of-a-kind")
            result["hand_highest"] = find_card_score(
                result["hand_highest"],
                CARD_SCORES[card]
            )
            threes += 1

        elif count == 2:
            result = set_hand_analysis(
                result, hand_name="pair")
            result["hand_highest"] = find_card_score(
                result["hand_highest"],
                CARD_SCORES[card]
            )
            pairs += 1

        # ? Sets highest card for Straights and High Cards
        elif not fours and not threes and not pairs:
            result["hand_highest"] = find_card_score(
                result["hand_highest"],
                CARD_SCORES[card]
            )

    # ? Threes and Pairs
    if threes == 1 and pairs == 1:
        result = set_hand_analysis(result, "full house")
    elif pairs == 2:
        result = set_hand_analysis(result, "two pair")

    # ? Straights and High Cards
    elif not fours and not threes and not pairs:
        sequence = sort_hand(hand_count)
        if len(sequence) == 5:
            start = sequence[0]
            if result["wildcard"]:
                end = sequence[3]
            else:
                end = sequence[4]

            if sequence[0] == "A" and (
                    sequence[1] == "K" or sequence[1] == "5"):
                if sequence[1] == "5":
                    result["hand_highest"] = CARD_SCORES["5"]
                start = sequence[1]
            else:
                start = sequence[0]

            difference = CARD_SCORES[start] - CARD_SCORES[end]

            if difference > 4:
                result = set_hand_analysis(result, "high card")
            else:
                result = set_hand_analysis(result, "straight")

    # ? Threes with wildcard
    elif threes == 1 and result["wildcard"]:
        result = set_hand_analysis(result, hand_name="four-of-a-kind")

    # ? Pair with wildcard
    elif pairs == 1 and result["wildcard"]:
        result = set_hand_analysis(
            result, hand_name="three-of-a-kind")

    # ! DEBUG
    # print("hand: {hand} - hand_class: {hand_class}, hand_score: {hand_score}, hand_highest: {hand_highest}, card_score: {card_score}".format(
    #     hand=hand, hand_class=result["hand_class"], hand_score=result[
    #         "hand_score"], hand_highest=result["hand_highest"], card_score=result["card_score"]
    # ))

    return result


def find_card_score(current_card_score, new_card_score):
    if new_card_score >= current_card_score:
        return new_card_score
    return current_card_score


def count_cards(hand):
    """returns a dict of counted cards; legally of course"""
    counts = {}
    for card in hand:
        if card not in counts:
            counts[card] = 1
        else:
            counts[card] += 1
    return counts


def valid_hand(hand):
    """Checks for valid input for hands"""
    wild_count = 0

    if not isinstance(hand, str):
        return False

    if len(hand) < 5 or len(hand) > 5:
        print(
            "Error: Hand `{hand}` invalid length!".format(
                hand=hand))
        return False

    for char in hand:
        if char not in CARD_SCORES.keys():
            return False
        else:
            if char == '*':
                wild_count += 1

    if wild_count > 1:
        return False

    return True


def sort_hand(hand):
    """Sorts hand by card value; desc"""

    return [
        tuple for x in CARD_SCORES.keys() for tuple in hand if tuple[0] == x]


def set_hand_analysis(analysis, hand_name=None):
    analysis["hand_class"] = hand_name
    analysis["hand_score"] = HAND_SCORES[hand_name]
    return analysis


if __name__ == '__main__':
    args = sys.argv[1:]
    hand_one = args[0]
    hand_two = args[1]
    main(hand_one, hand_two)
