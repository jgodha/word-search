import unittest
from WordSearch import search


class WordSearchTest(unittest.TestCase):
    grid = [
            ['z', 'y', 'x', 'w', 'v'],
            ['a', 'r', 'a', 't', 's'],
            ['p', 'b', 'a', 't', 'o'],
            ['n', 'm', 'l', 'k', 'j'],
            ['i', 'h', 'g', 'b', 'e']
    ]

    def test_word_horizontal_forward_every_letter_occurs_once(self):
        result = search([['a', 'b'], ['c', 'd']], "ab")
        self.assertEqual("ab: (0,0)(0,1)", result)

    def test_word_horizontal_forward_multiple_occurrences(self):
        result = search(self.grid, "bat")
        self.assertEqual("bat: (2,1)(2,2)(2,3)", result)

    def test_word_horizontal_backward(self):
        result = search(self.grid, "star")
        self.assertEqual("star: (1,4)(1,3)(1,2)(1,1)", result)


if __name__ == '__main__':
    unittest.main()
