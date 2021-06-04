class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        ### method 1 ### 
        '''
        self.temp = [] 
        pu = 0 
        pp = 0 
        while pp <len(popped):
            if popped[pp] not in self.temp and pu <len(pushed):
                self.push(self.temp, pushed[pu])
                pu+=1 
            elif popped[pp] in self.temp and self.temp[-1] == popped[pp]:
                self.pop(self.temp)
                pp += 1
            elif popped[pp] in self.temp and self.temp[-1] != popped[pp]:
                return False 
            elif popped[pp] not in self.temp and pu >= len(pushed):
                return False
        '''
        ### method 2 ###
        j = 0 
        self.temp = []
        for i in range(len(pushed)):
            self.push(self.temp, pushed[i])
            while self.temp and popped[j] == self.temp[-1]:
                j+= 1
                self.pop(self.temp)

        return not self.temp     
    def pop(self, stack):
        if stack:
            return stack.pop()
    def push(self, stack,x ):
        return stack.append(x)
