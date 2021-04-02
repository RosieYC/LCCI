class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        res = S[:length].split(' ')
        res = '%20'.join(res)
        return res
