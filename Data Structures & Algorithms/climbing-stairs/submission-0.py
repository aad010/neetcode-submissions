class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def memoization(n):
            if n == 0:
                return 1
            elif n < 0:
                return 0
            if n in cache:
                return cache[n]
            else:
                cache[n] = memoization(n - 1) + memoization(n - 2)
                return cache[n]
        
        return memoization(n)