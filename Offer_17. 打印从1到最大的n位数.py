import numpy as np
class Solution:
    def myPow(self, n: int) -> float:
        res = 1 
        x = 10
        while n:
            if n&1: 
                res *= x 
            x *= x 
            n>>=1 
        return res
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1, self.myPow(n)))
