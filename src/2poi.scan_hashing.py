import unittest

def plant_pumpkins(m, n, pumpkins):
    return [pumpkins[i][j] for i in range(m) for j in range(n)] if m % 2 == 0 else [pumpkins[i][j] for i in range(m) for j in range(n-1, -1, -1)]

class TestPlantPumpkins(unittest.TestCase):

    def test_m_equals_n_equals_5(self):
        m = 5
        n = 5
        pumpkins = [[1, 2, 3, 4, 5],
                    [10, 9, 8, 7, 6],
                    [11, 12, 13, 14, 15],
                    [20, 19, 18, 17, 16],
                    [21, 22, 23, 24, 25]]
        expected_result = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 15, 14, 13, 12, 11, 16, 17, 18, 19, 20, 25, 24, 23, 22, 21]
        self.assertEqual(plant_pumpkins(m, n, pumpkins), expected_result)

    def test_m_equals_2_n_equals_4(self):
        m = 2
        n = 4
        pumpkins = [[1, 2, 3, 4],
                    [8, 7, 6, 5]]
        expected_result = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(plant_pumpkins(m, n, pumpkins), expected_result)

    def test_n_equals_1_m_equals_6(self):
        m = 6
        n = 1
        pumpkins = [[1],
                    [2],
                    [3],
                    [4],
                    [5],
                    [6]]
        expected_result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(plant_pumpkins(m, n, pumpkins), expected_result)

if __name__ == "__main__":
    unittest.main()
