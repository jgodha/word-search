import unittest
from WordSearch import search


class WordSearchTest(unittest.TestCase):
    grid = [
            ['z', 'y', 'x', 'y', 'v'],
            ['a', 'r', 'a', 't', 's'],
            ['p', 'b', 'a', 't', 'o'],
            ['n', 'm', 's', 'e', 'j'],
            ['i', 'h', 'k', 'b', 'e']
    ]

    def test_word_search_horizontal_forward_every_letter_occurs_once(self):
        result = search([['a', 'b'], ['c', 'd']], "ab")
        self.assertEqual("ab: (0,0)(0,1)", result)

    def test_word_search_horizontal_forward_multiple_occurrences(self):
        result = search(self.grid, "bat")
        self.assertEqual("bat: (2,1)(2,2)(2,3)", result)

    def test_word_search_horizontal_backward(self):
        result = search(self.grid, "star")
        self.assertEqual("star: (1,4)(1,3)(1,2)(1,1)", result)

    def test_word_search_horizontal_start_letter_first_occurrence_not_used(self):
        result = search(self.grid, "tab")
        self.assertEqual("tab: (2,3)(2,2)(2,1)", result)

    def test_word_search_vertical_downward(self):
        result = search(self.grid, "ask")
        self.assertEqual("ask: (2,2)(3,2)(4,2)", result)

    def test_word_search_vertical_upward(self):
        result = search(self.grid, "betty")
        self.assertEqual("ask: (4,3)(3,3)(2,3)(1,3)(0,3)", result)


if __name__ == '__main__':
    unittest.main()
