class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict_ ={
            '0': '', 
            '1': '',
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        if digits == "":
            return []
        i =1 
        answer = list(dict_[digits[0]])
        def recursive(dig_len, string1, string2):
            temp = []
            for k in range(len(string1)):
                for j in range(len(string2)):
                    temp.append(string1[k]+string2[j])
            return temp
        while i+1 <= len(digits):
            answer = recursive(i, answer, dict_[digits[i]])
            i+= 1 
        return answer
            
