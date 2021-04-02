class Solution:
    def compressString(self, S: str) -> str:
        if len(S) == 0:
            return ''
        temp = S[0] 
        index = 0
        res = temp
        for i in range(1, len(S)):
            if temp != S[i]:
                temp = S[i]
                res += str(i-index)
                res += temp
                index = i
        res += str(len(S)-index)
        return res if len(res) < len(S) else S
