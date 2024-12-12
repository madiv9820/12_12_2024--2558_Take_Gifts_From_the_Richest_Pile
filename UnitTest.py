from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: ([25,64,9,4,100], 4, 29), 2: ([1,1,1,1], 4, 4)}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_1(self):
        gifts, k, output = self.__testCases[1]
        result = self.__obj.pickGifts(gifts, k)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_2(self):
        gifts, k, output = self.__testCases[2]
        result = self.__obj.pickGifts(gifts, k)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()