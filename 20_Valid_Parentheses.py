class Solution:
    def isValid(self, s: str) -> bool:
        standard = ['[]', '()', '{}']
        stack = list(s)
        if len(stack)%2 != 0:
            return False
        temp = []
        for i in stack:
            if len(temp) == 0:
                temp.append(i)
                temp_idx = 0
            else:
                last = temp.pop()
                if last+i not in standard:
                    temp.append(last)
                    temp.append(i)
        if len(temp) == 0:
            return True
        return False
