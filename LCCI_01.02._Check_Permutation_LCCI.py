class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        count = Counter(list(s1))
        count2 = Counter(list(s2))
        if count == count2:
            return True
        return False
