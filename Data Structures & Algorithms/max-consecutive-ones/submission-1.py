class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_list = [0] * len(nums) 
        counter = 0
        index = 0

        for i, element in enumerate(nums):
            if element == 1:
                counter+=1
                max_list[index] = counter
            else:
                counter = 0
                index += 1

        return max(max_list)
