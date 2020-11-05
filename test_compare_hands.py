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
        self.assertEqual(
            compare_hands.valid_hand("AAAAKA"),
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
            compare_hands.compare_hands("A267J", "KQJT6"),
            "A267J vs KQJT6: A267J high card > KQJT6 high card"
        )

    def test_analyze_hand_eight(self):
        self.assertEqual(
            compare_hands.compare_hands("3579*", "A2345"),
            "3579* vs A2345: 3579* high card < A2345 straight"
        )

    def test_analyze_hand_nine(self):
        self.assertEqual(
            compare_hands.compare_hands("2357A", "AKQJT"),
            "2357A vs AKQJT: 2357A high card < AKQJT straight"
        )

    def test_analyze_hand_ten(self):
        self.assertEqual(
            compare_hands.compare_hands("*789T", "*2345"),
            "*789T vs *2345: *789T straight > *2345 straight"
        )

    def test_analyze_hand_eleven(self):
        self.assertEqual(
            compare_hands.compare_hands("AAA*5", "AA*45"),
            "AAA*5 vs AA*45: AAA*5 four-of-a-kind > AA*45 three-of-a-kind"
        )


if __name__ == '__main__':
    unittest.main()
