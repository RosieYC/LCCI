class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        pre = 0
        last = len(nums)-1
        while last > pre:
            while pre <= len(nums)-1 and nums[pre]%2 ==1 :
                pre += 1 
            while last >=0 and nums[last]%2==0  :
                last-=1
            if last > pre:
                temp = nums[last]
                nums[last] = nums[pre]
                nums[pre] = temp
        return nums
