import unittest
import random_forest


class TestRandomForest(unittest.TestCase):

    def test_calculate_random_forest(self):
        rf = random_forest.RandomForest()
        self.assertIsNotNone(rf.get())

    def test_randomness(self):
        rf = random_forest.RandomForest()
        forests = set([rf.get() for _ in range(0, 100)])
        # Out of a hundred random forests, we should at least get more than one forest.
        self.assertTrue(len(forests) > 1)


if __name__ == '__main__':
    unittest.main()
