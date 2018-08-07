import unittest
from WordSearch import WordSearch

class WordSearchTest(unittest.TestCase):
    def test_word_horizontal_forward(self):
        result = WordSearch.search([['a', 'b','c'], ['d', 'e', 'f'], ['g', 'h', 'i']] , ["ab"])
        self.assertEqual(result, "foo")

if __name__ == '__main__':
    unittest.main()
