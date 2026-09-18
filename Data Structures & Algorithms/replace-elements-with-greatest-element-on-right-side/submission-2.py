class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Brute Force O(n^2)
        # max_element = 0
        # for i in range(len(arr)):
        #     j = i + 1
        #     if i == len(arr) - 1:
        #         arr[i] = -1
        #         return arr

        #     while j < len(arr):
        #         max_element = max(arr[j], max_element)
        #         j += 1
            
        #     arr[i] = max_element
        #     max_element = 0

        # Better Solution O(n)
        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(arr[i], rightMax)
            arr[i] = rightMax
            rightMax = newMax
            
        return arr