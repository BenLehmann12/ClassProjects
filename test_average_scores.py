import unittest
import unittest.mock as mock
import format_output.average_scores as avg_score
class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85,90,95]):
            assert avg_score.average() == 90

if __name__ == '__main__':
    unittest.main()
    def average():
        score1 = int(input("Enter first score:"))
        score2 = int(input("Enter second score:"))
        score3 = int(input("Enter third score:"))
        sum = score1+score2+score3
        avg = sum/3
        return avg
