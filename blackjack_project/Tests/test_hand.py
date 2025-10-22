import unittest
from Code.hand import Hand
from unittest.mock import patch

@patch.object(Hand, 'get_card')
class TestHandMethods(unittest.TestCase):
    def test_regular_cards(self, cards):
        cards.side_effect = ["2","3"]
        hand = Hand()

        self.assertEqual(hand.total, 5)
        self.assertEqual(hand.soft_total, 5)

    def test_face_cards_1(self, cards):
        cards.side_effect = ["T","J"]
        hand = Hand()

        self.assertEqual(hand.total, 20)
        self.assertEqual(hand.soft_total, 20)

    def test_face_cards_2(self, cards):
        cards.side_effect = ["Q","K"]
        hand = Hand()

        self.assertEqual(hand.total, 20)
        self.assertEqual(hand.soft_total, 20)
    
    def test_ace(self, cards):
        cards.side_effect = ["A","5"]
        hand = Hand()

        self.assertEqual(hand.total, 6)
        self.assertEqual(hand.soft_total, 16)

    def test_two_aces(self, cards):
        cards.side_effect = ["A","A"]
        hand = Hand()

        self.assertEqual(hand.total, 2)
        self.assertEqual(hand.soft_total, 12)
    
    def test_three_aces(self, cards):
        cards.side_effect = ["A","A","A"]
        hand = Hand()
        hand.hit()

        self.assertEqual(hand.total, 3)
        self.assertEqual(hand.soft_total, 13)
    
    def test_blackjack(self, cards):
        cards.side_effect = ["A","J"]
        hand = Hand()

        self.assertEqual(hand.total, 11)
        self.assertEqual(hand.soft_total, 21)
        self.assertTrue(hand.check_for_blackjack())

    
if __name__ == '__main__':
    unittest.main()