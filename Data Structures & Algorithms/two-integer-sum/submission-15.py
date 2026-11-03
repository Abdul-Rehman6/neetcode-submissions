class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Two pointers require a sorted array, but sorting nums loses the original indices.
        # We can preserve them using [value, original_index]:

        # arr = [[num, i] for i, num in enumerate(nums)]
        # arr.sort()

        # This works in O(n log n) time and O(n) space.
        # Better approach: Hash Map -> O(n) time and O(n) space.

        # j = 0
        # i = len(nums) - 1
        # while j < i:
        #     if nums_copy[i] + nums_copy[j] == target:
                
        #         return [j, i]
        #     elif nums_copy[i] + nums_copy[j] < target:
        #         j += 1
        #     elif nums_copy[i] + nums_copy[j] > target:
        #         i -= 1
        # return []

        hash_map = {}

        for i in range(len(nums)):
            needed_element = target - nums[i]

            if needed_element in hash_map:
                return [hash_map[needed_element], i]

            hash_map[nums[i]] = i
            
        return []

