class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = ""
        if len(s) == numRows or numRows == 1:
            return s
        interval = numRows * 2 - 2 # 4 
        for j in range(numRows):
            for i in range(len(s)//interval+2):
                temp = interval * i - j, interval * i+j
                if temp[0] >=len(s):
                    continue
                if j == numRows-1 :
                    if temp[0] <0:
                        continue
                    answer += s[temp[0]]
                elif temp[0] < 0 and temp[1] < len(s) :
                    answer += s[temp[1]]
                elif temp[0] >=0 and temp[1] >= len(s) and j != 0:
                    answer += s[temp[0]]
                elif temp[0] >=0 and temp[1] <len(s):
                    if temp[0] != temp[1]:
                        answer += s[temp[0]]
                    answer += s[temp[1]]
        return answer        
