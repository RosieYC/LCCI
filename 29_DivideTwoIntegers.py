# https://blog.csdn.net/zhou_yujia/article/details/83000205
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 0 
        flag = 1 
        if (dividend * divisor) < 0:
            flag = -1 
        dividend, divisor = abs(dividend), abs(divisor)
        tot, p, q = 0, 1, divisor
        while(dividend>=divisor):
            if dividend>=q:
                tot += p
                dividend-=q 
                p = p<<1 
                q = q<<1
            else:
                p = p>>1 
                q = q>>1 
        return min(max(-2147483648, tot*flag), 2147483647)
    
