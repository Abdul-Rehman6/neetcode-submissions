class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_element = 0
        for i in range(len(arr)):
            j = i + 1
            if i == len(arr) - 1:
                arr[i] = -1
                return arr
                
            while j < len(arr):
                max_element = max(arr[j], max_element)
                j += 1
            
            arr[i] = max_element
            max_element = 0