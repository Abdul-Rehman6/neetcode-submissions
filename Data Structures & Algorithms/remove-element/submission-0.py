class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_copy = nums.copy()

        for element in nums_copy:
            if element == val:
                nums.remove(element)
        
        return len(nums)