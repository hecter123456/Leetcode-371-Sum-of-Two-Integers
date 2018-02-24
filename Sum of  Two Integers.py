import unittest

class unitest(unittest.TestCase):
    def testSample(self):
        a = 1
        b = 2
        Output = 3
        self.assertEqual(Solution().getSum(a,b),Output)
    def testMoveCase(self):
        a = 1
        b = 1
        Output = 2
        self.assertEqual(Solution().getSum(a,b),Output)
    def testNegetive(self):
        a = -1
        b = -1
        Output = -2
        self.assertEqual(Solution().getSum(a,b),Output)
class Solution():
    def getSum(self, a, b):
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while(b):
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= MAX else ~(a ^ mask)

if __name__ == '__main__':
    unittest.main()
