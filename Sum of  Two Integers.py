import unittest

class unitest(unittest.TestCase):
    def testSample(self):
        a = 1
        b = 2
        Output = 3
        self.assertEqual(Solution().getSum(a,b),Output);

class Solution():
    def getSum(self, a, b):
        ans = 0
        move = 0
        while(a != 0 or b != 0):
            ans = ans << 1
            ans |= (a%2) ^ (b%2) ^ move
            move = ((a%2) & (b%2)) ^ ((a%2) & move) ^ (move & (b%2))
            a = a >> 1
            b = b >> 1
        return ans

if __name__ == '__main__':
    unittest.main()
