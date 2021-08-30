class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        first = 0 
        end = len(nums)-1 
        answer = []
        if len(nums)<4:
            return []
        for i in range(0, len(nums)-3, 1):
            for j in range(end, 2, -1):
                temp = target - (nums[i] + nums[j])
                second = i+1
                third = j-1
                while second <third:
                    if nums[second] + nums[third] > temp:
                        third -=1
                    elif nums[second] + nums[third] < temp:
                        second += 1 
                    else:
                        if [nums[i], nums[second], nums[third], nums[j]] not in answer:
                            answer.append([nums[i], nums[second], nums[third], nums[j]])
                        second += 1 
                        third -=1
    
        return answer