class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first)-len(second)) >1:
            return False
        for i in range(0, min(len(first), len(second))):
            if first[i] != second[i]:
                return first[i+1:]==second[i+1:] or first[i+1:]==second[i:] or first[i:]==second[i+1:]
        return True
