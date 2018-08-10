import unittest
from WordSearch import WordSearch

class WordSearchTest(unittest.TestCase):
    def test_word_horizontal_forward(self):
        result = WordSearch.search([['a', 'b'], ['c', 'd']] , ["ab"])
        self.assertEqual(result, ["ab: (0,0), (1,0)"])

if __name__ == '__main__':
    unittest.main()
