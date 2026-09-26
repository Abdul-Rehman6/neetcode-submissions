class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counting_hash_map = {}
        return_list = []
        i = 0

        for element in nums:
            if element in counting_hash_map:
                counting_hash_map[element] += 1
            else:
                counting_hash_map[element] = 1

        sorted_list = sorted(counting_hash_map, key=counting_hash_map.get, reverse=True)

        while i < k:
            element = sorted_list[i]
            return_list.append(element)
            i += 1
        
        return return_list