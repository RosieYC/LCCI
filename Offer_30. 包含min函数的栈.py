class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
    def min(self) -> int:
        if self.stack:
            return min(self.stack)
        

            
        
         



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
