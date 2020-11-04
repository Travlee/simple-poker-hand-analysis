#!/usr/bin/python3

import unittest
import compare_hands


class TestCompareHands(unittest.TestCase):

    def test_valid_hand_wildcards(self):
        """Tests valid hand with wildcards"""
        self.assertEqual(
            compare_hands.valid_hand("234**"),
            False
        )
        self.assertEqual(
            compare_hands.valid_hand("2345*"),
            True
        )

    def test_valid_hand_chars(self):
        """Tests valid hands"""
        self.assertEqual(
            compare_hands.valid_hand("AAAKT"),
            True
        )
        self.assertEqual(
            compare_hands.valid_hand("AAAKG"),
            False
        )
        self.assertEqual(
            compare_hands.valid_hand(1),
            False
        )

    def test_analyze_hand_one(self):
        self.assertEqual(
            compare_hands.compare_hands("AAAKT", "22233"),
            "AAAKT vs 22233: AAAKT three-of-a-kind < 22233 full house"
        )

    def test_analyze_hand_two(self):
        self.assertEqual(
            compare_hands.compare_hands("AA223", "KKQQT"),
            "AA223 vs KKQQT: AA223 two pair > KKQQT two pair"
        )

    def test_analyze_hand_three(self):
        self.assertEqual(
            compare_hands.compare_hands("2345*", "KKJJ2"),
            "2345* vs KKJJ2: 2345* straight > KKJJ2 two pair"
        )

    def test_analyze_hand_four(self):
        self.assertEqual(
            compare_hands.compare_hands("AAKKT", "AAKKT"),
            "AAKKT vs AAKKT: AAKKT two pair == AAKKT two pair"
        )

    def test_analyze_hand_five(self):
        self.assertEqual(
            compare_hands.compare_hands("KKKKA", "KKKK*"),
            "KKKKA vs KKKK*: KKKKA four-of-a-kind == KKKK* four-of-a-kind"
        )

    def test_analyze_hand_six(self):
        self.assertEqual(
            compare_hands.compare_hands("AA234", "AA235"),
            "AA234 vs AA235: AA234 pair < AA235 pair"
        )

    def test_analyze_hand_six(self):
        self.assertEqual(
            compare_hands.compare_hands("AA99K", "AA88K"),
            "AA99K vs AA88K: AA99K two pair > AA88K two pair"
        )

    def test_analyze_hand_seven(self):
        self.assertEqual(
            compare_hands.compare_hands("A267J", "KQJT1"),
            "A267J vs KQJT1: A267J high card > KQJT1 high card"
        )

    def test_analyze_hand_eight(self):
        self.assertEqual(
            compare_hands.compare_hands("1357*", "A2345"),
            "1357* vs A2345: 1357* high card < A2345 straight"
        )

    def test_analyze_hand_nine(self):
        self.assertEqual(
            compare_hands.compare_hands("1357A", "AKQJT"),
            "1357A vs AKQJT: 1357A high card < AKQJT straight"
        )

    def test_analyze_hand_ten(self):
        self.assertEqual(
            compare_hands.compare_hands("*789T", "*1234"),
            "*789T vs *1234: *789T straight > *1234 straight"
        )


if __name__ == '__main__':
    unittest.main()
