import unittest
import dijkstra


class TestDijkstra(unittest.TestCase):
    def test_roa2021(self):
        value = {
            'S': {'a': 5, 'b': 2},
            'a': {'b': 8, 'c': 4, 'd': 1},
            'b': {'c': 5, 'd': 7},
            'c': {'d': 6, 'G': 3},
            'd': {'G': 2},
            'G': {}
        }
        expected = (8, ['S', 'a', 'd', 'G'])
        actual = dijkstra.solve(value, 'S', 'G')
        self.assertEqual(expected, actual)

    def test_one(self):
        value = {
            'S': {'a': 1, 'b': 2},
            'a': {'b': 8, 'c': 2, 'd': 1},
            'b': {'c': 5, 'd': 7},
            'c': {'d': 6, 'G': 1},
            'd': {'G': 2},
            'G': {}
        }
        expected = (4, ['S', 'a', 'c', 'G'])
        actual = dijkstra.solve(value, 'S', 'G')
        self.assertEqual(expected, actual)

    def test_two(self):
        value = {
            'S': {'a': 1, 'b': 1},
            'a': {'b': 1, 'c': 9, 'd': 4},
            'b': {'c': 1, 'd': 7},
            'c': {'d': 1, 'G': 4},
            'd': {'G': 1},
            'G': {}
        }
        expected = (4, ['S', 'b', 'c', 'd', 'G'])
        actual = dijkstra.solve(value, 'S', 'G')
        dijkstra.show(value, actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
