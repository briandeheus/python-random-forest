import unittest
import random_forest


class TestRandomForest(unittest.TestCase):

    def test_calculate_random_forest(self):
        rf = random_forest.RandomForest()
        self.assertIsNotNone(rf.get())


if __name__ == '__main__':
    unittest.main()
