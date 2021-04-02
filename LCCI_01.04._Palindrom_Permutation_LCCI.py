class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odd = 0 
        counter = Counter(s)
        nsmallest = sorted(counter.items(), key=itemgetter(1), reverse=False)

        for _, c in nsmallest:
            if c %2== 1 :
                odd += 1
            if odd >=2 :
                return False
        if odd == 1 and len(s) %2 == 1:
            return True    
        return True
