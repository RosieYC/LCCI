class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) == len(s2) == 0:
            return True
        s3 = s2+ s2
        for i in range(len(s3)):
            if s3[i] == s1[0]:
                if s3[i:i+len(s2)] == s1:
                    return True
        return False
