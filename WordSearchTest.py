import unittest
from WordSearch import search


class WordSearchTest(unittest.TestCase):
    def test_word_horizontal_forward(self):
        result = search([['a', 'b'], ['c', 'd']], "ab")
        self.assertEqual(result, "ab: (0,0)(0,1)")


if __name__ == '__main__':
    unittest.main()
